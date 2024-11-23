from flask import Flask, request, render_template
import os
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

# 初始化Tkinter
root = tk.Tk()
root.withdraw()

# 弹出文件夹选择对话框
UPLOAD_FOLDER = filedialog.askdirectory(title="选择图片保存路径")

if not UPLOAD_FOLDER:
    UPLOAD_FOLDER = 'uploads'
    print("未选择路径，默认保存到uploads目录下")
    # exit()

app = Flask(__name__)

# 定义端口号
server_port = '80'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index3.html')

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
    print(f'图片保存路径是：{UPLOAD_FOLDER}')
    app.run(debug=False, host='0.0.0.0', port=server_port)
