async function processImage() {
    const input = document.getElementById('image-input').files[0];
    const formData = new FormData();
    formData.append('image', input);

    const response = await fetch('/ocr', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('image-output').innerText = result.text;
}

async function processAudio() {
    const input = document.getElementById('audio-input').files[0];
    const formData = new FormData();
    formData.append('audio', input);

    const response = await fetch('/speech-to-text', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('audio-output').innerText = result.text;
}

async function processTTS() {
    const input = document.getElementById('tts-input').value;
    const response = await fetch('/text-to-speech', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: input })
    });
    const result = await response.json();
    alert(result.message);
    document.getElementById('tts-output').src = 'output.mp3';
}

async function processDocx() {
    const input = document.getElementById('docx-input').files[0];
    const formData = new FormData();
    formData.append('document', input);

    const response = await fetch('/docx-to-text', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('docx-output').innerText = result.text;
}

async function processPdf() {
    const input = document.getElementById('pdf-input').files[0];
    const formData = new FormData();
    formData.append('document', input);

    const response = await fetch('/pdf-to-text', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('pdf-output').innerText = result.text;
}

async function translateText() {
    const input = document.getElementById('translate-input').value;
    const srcLang = document.getElementById('src-lang').value;
    const destLang = document.getElementById('dest-lang').value;

    const response = await fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: input, src_lang: srcLang, dest_lang: destLang })
    });
    const result = await response.json();
    document.getElementById('translate-output').innerText = result.translated_text;
}
