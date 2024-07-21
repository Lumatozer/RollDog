from flask import request, redirect
from monster import render, tokeniser, parser, Flask
import sys, json
import os

app = Flask(__name__)

@app.get("/")
def home():
    tailwind=open("public/tailwind.js").read()
    maincss=open("public/main.css").read()
    computer=render("computer", locals())
    return render("index", locals())

app.run(host="0.0.0.0", port=int(sys.argv[1]))