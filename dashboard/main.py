from flask import request, redirect
from monster import render, tokeniser, parser, Flask
import sys, json
import os

os.system("sudo xhost +SI:localuser:teachers")

app = Flask(__name__)

@app.get("/")
def home():
    signals=open("public/signals.js").read()
    print(tokeniser(open("components/index.html").read()))
    print(parser(tokeniser(open("components/index.html").read())))
    return render("index", locals())

app.run(host="0.0.0.0", port=int(sys.argv[1]))