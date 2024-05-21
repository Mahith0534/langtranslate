from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
from PIL import Image
import speech_recognition as sr
import pyttsx3
from docx import Document
import PyPDF2
from googletrans import Translator
import io
import os

app = Flask(__name__)
CORS(app)

# OCR from image
@app.route('/ocr', methods=['POST'])
def ocr_from_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files['image']
    img = Image.open(file.stream)
    text = pytesseract.image_to_string(img)
    return jsonify({"text": text})

# Speech to text
@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    file = request.files['audio']
    recognizer = sr.Recognizer()
    audio = sr.AudioFile(file.stream)

    with audio as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return jsonify({"text": text})
    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand the audio"}), 400
    except sr.RequestError:
        return jsonify({"error": "Google API error"}), 500

# Text to speech
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

# DOCX to text
@app.route('/docx-to-text', methods=['POST'])
def docx_to_text():
    if 'document' not in request.files:
        return jsonify({"error": "No document provided"}), 400
    
    file = request.files['document']
    doc = Document(file.stream)
    full_text = [para.text for para in doc.paragraphs]
    return jsonify({"text": '\n'.join(full_text)})

# PDF to text
@app.route('/pdf-to-text', methods=['POST'])
def pdf_to_text():
    if 'document' not in request.files:
        return jsonify({"error": "No document provided"}), 400
    
    file = request.files['document']
    reader = PyPDF2.PdfFileReader(file.stream)
    full_text = [reader.getPage(page_num).extract_text() for page_num in range(reader.numPages)]
    return jsonify({"text": '\n'.join(full_text)})

# Translation
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
