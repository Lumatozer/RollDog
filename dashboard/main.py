from flask import request, redirect
from monster import render, tokeniser, parser, Flask
import sys, json
import os

app = Flask(__name__)

@app.get("/")
def home():
    signals=open("public/signals.js").read()
    ip="http://127.0.0.1:1234"
    indexjs=render("public/index.js", locals())
    return render("index", locals())

app.run(host="0.0.0.0", port=int(sys.argv[1]))