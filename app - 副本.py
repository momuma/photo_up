from flask import Flask, request, render_template
import os

app = Flask(__name__)

# 设置保存图片的路径
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
