from flask import Flask, send_file
from werkzeug.utils import safe_join
import base64

app=Flask(__name__)

def sanitize(s):
    return "".join([x for x in s if x in "abcdefghijklmnopqrstuvwxyz-"])

@app.route('/install/<path:path>')
def installer(path):
    if len(sanitize(path))!=len(path):
        return "path is not safe"
    return open("installers/"+sanitize(path)+"/install.py").read().replace("{server_main.py}", base64.b64encode(open("../"+sanitize(path)+"/main.py").read().encode()).decode())

app.run(host="0.0.0.0", port=8080)