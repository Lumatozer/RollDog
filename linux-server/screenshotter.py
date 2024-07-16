from PIL import ImageGrab
from flask import Flask, send_file
import time
import threading
import os

app=Flask(__name__)

def regular_catcher():
    while True:
        time.sleep(5)
        ss=ImageGrab.grab()
        ss.save("screenshots/"+str(int(time.time()))+".png", "png")
        images=sorted([{"id":int(x.split(".")[0]), "path":x} for x in os.listdir("screenshots")], key=lambda x:x["id"])
        if len(images)>27000:
            for x in images[:len(images)-27000]:
                os.system("sudo rm screenshots/"+x["path"])

threading.Thread(target=regular_catcher).start()

@app.get("/")
def home():
    ss=ImageGrab.grab()
    filename="screenshots/"+str(time.time())+".png"
    ss.save(filename, "png")
    return send_file(filename)

app.run(host="0.0.0.0", port=5000)