from flask import Flask, render_template, request, send_file
from gtts import gTTS, lang

app = Flask(__name__)

@app.route('/')
def index():
    languages = lang.tts_langs()
    return render_template('index.html', languages=languages)

@app.route('/download', methods=['POST'])
def download():
    text = request.form['text']
    language = request.form['language']
    tts = gTTS(text, lang=language)
    tts.save('output.mp3')
    return send_file('output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run()
