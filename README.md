# TranslateX

TranslateX is a powerful and easy-to-use application that allows users to **upload files (Images, PDFs, Audio, Word documents)**, **extract text**, **translate** it into regional languages (Hindi, Marathi, Bengali, Gujarati, Tamil, Telugu), and **save** the output as a **Word Document** (`.docx`) or **Audio File** (`.mp3`).

The app is built using **Tkinter** for GUI, and uses **Tesseract OCR**, **Speech Recognition**, **Google Translate**, and **gTTS** (Google Text-to-Speech).

---

## Features ✨

- Upload **Image**, **PDF**, **Audio**, or **DOCX** files.
- Automatically extract text from the uploaded file.
- Translate text into **regional Indian languages**.
- Save translated text as a `.docx` file or `.mp3` audio file.
- Clean and simple **Tkinter** based user interface.

---

## How to Run 🚀

1. **Clone this repository**:
   ```bash
   git clone https://github.com/Mahith0534/langtranslate.git
   cd translatex
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Required packages:
   - tkinter (comes pre-installed with Python)
   - pytesseract
   - pdfplumber
   - SpeechRecognition
   - googletrans==4.0.0-rc1
   - python-docx
   - gTTS
   - pillow

   Also install Tesseract OCR engine separately:
   - [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract)

3. **Run the app**:
   ```bash
   python app.py
   ```

---

## Folder Structure 📁

```
TranslateX/
├── project.py     # Main Python application
├── README.md      # Project documentation
├── requirements.txt
```

---

## Future Scope 🚀

- **Migrate UI to Streamlit** or **Gradio** for a modern, web-based interface.
- **Add more languages** and auto-detection of source language.
- **Drag and Drop** feature for easier file uploads.
- **Batch processing** of multiple files at once.
- **Summarization** of extracted text before translation.
- **Voice playback** of translated text inside the app itself.
- **Save history** of previous translations.

---

## Credits 📚

- [pytesseract](https://github.com/madmaze/pytesseract)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [googletrans](https://pypi.org/project/googletrans/)
- [gTTS](https://pypi.org/project/gTTS/)
- [python-docx](https://python-docx.readthedocs.io/en/latest/)

---

## License 📝

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

