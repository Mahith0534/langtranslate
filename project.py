from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image
import speech_recognition as sr
import pyttsx3
from docx import Document
from PyPDF2 import PdfReader
from googletrans import Translator
import pytesseract
from pydub import AudioSegment
import io

# Set the tesseract command to the full path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust path for your system

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ocr', methods=['POST'])
def ocr_from_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files['image']
    img = Image.open(file.stream)
    text = pytesseract.image_to_string(img)
    return jsonify({"text": text})

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    file = request.files['audio']
    recognizer = sr.Recognizer()

    try:
        # Attempt to open the audio file using pydub
        audio = AudioSegment.from_file(file.stream)
        # Convert the audio to a format that SpeechRecognition can handle
        wav_io = io.BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)
        audio_data = sr.AudioFile(wav_io)

        with audio_data as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    engine = pyttsx3.init()
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()

    return jsonify({"message": "Speech saved as output.mp3"})

@app.route('/docx-to-text', methods=['POST'])
def docx_to_text():
    if 'document' not in request.files:
        return jsonify({"error": "No document provided"}), 400
    
    file = request.files['document']
    doc = Document(file.stream)
    full_text = [para.text for para in doc.paragraphs]
    return jsonify({"text": '\n'.join(full_text)})

@app.route('/pdf-to-text', methods=['POST'])
def pdf_to_text():
    if 'document' not in request.files:
        return jsonify({"error": "No document provided"}), 400
    
    file = request.files['document']
    reader = PdfReader(file.stream)
    full_text = [page.extract_text() for page in reader.pages]
    return jsonify({"text": '\n'.join(full_text)})

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')
    src_lang = data.get('src_lang', 'en')
    dest_lang = data.get('dest_lang', 'es')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return jsonify({"translated_text": translated.text})

if __name__ == '__main__':
    app.run(debug=True)
