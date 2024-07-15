from flask import Flask, send_file
from werkzeug.utils import safe_join
import base64
import io
import zipfile, os

app=Flask(__name__)

def sanitize(s):
    return "".join([x for x in s if x in "abcdefghijklmnopqrstuvwxyz-"])

def zipup_folder(folder):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, folder))
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                zip_file.write(dir_path, os.path.relpath(dir_path, folder))
    return zip_buffer.getvalue()

@app.route('/install/<path:path>')
def installer(path):
    if len(sanitize(path))!=len(path):
        return "path is not safe"
    return open("installers/"+sanitize(path)+"/install.py").read().replace("{server_zip}", base64.b64encode(zipup_folder("../"+sanitize(path))).decode())

app.run(host="0.0.0.0", port=8080)