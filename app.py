from flask import Flask, render_template, request, send_file
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    text = request.form['text']
    tts = gTTS(text)
    tts.save('output.mp3')
    return send_file('output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run()
