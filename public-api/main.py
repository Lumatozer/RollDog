from flask import Flask, send_file
from werkzeug.utils import safe_join

app=Flask(__name__)

def sanitize(s):
    return "".join([x for x in s if x in "abcdefghijklmnopqrstuvwxyz-"])

@app.route('/install/<path:path>')
def installer(path):
    return send_file("installers/"+sanitize(path)+"/install.py")

app.run(host="0.0.0.0", port=8080)