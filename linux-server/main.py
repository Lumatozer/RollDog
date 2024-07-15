from flask import Flask

app=Flask(__name__)

@app.get("/")
def home():
    return "hi"

app.run(host="0.0.0.0", port=5000)