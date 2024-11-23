from flask import Flask, request, render_template
import os
from datetime import datetime


app = Flask(__name__)

# 定义端口号
server_port = '80'

# 设置保存图片的路径
# UPLOAD_FOLDER = 'uploads'
UPLOAD_FOLDER =r'c:\uploads'

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
    
    # 获取当前时间并格式化
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{timestamp}.jpg"  # 你可以根据需要更改扩展名
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return 'File uploaded successfully'

if __name__ == '__main__':
    print('图片保存路径是：c:\\uploads,你可以直接修改app2.py中图片保存路径')
    app.run(debug=True, host='0.0.0.0', port=server_port)
