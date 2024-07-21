from flask import request, redirect
from monster import render, tokeniser, parser, Flask
import sys, json
import os

app = Flask(__name__)

@app.get("/")
def home():
    signals=open("public/signals.js").read()
    indexjs=open("public/index.js").read()
    ip="127.0.0.1:7777"
    return render("index", locals())

app.run(host="0.0.0.0", port=int(sys.argv[1]))