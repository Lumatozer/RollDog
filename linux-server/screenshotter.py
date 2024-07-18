from PIL import ImageGrab
from flask import Flask, send_file, request, Response
import time
import threading
import hashlib
import secrets_parser
import pyautogui
import os

os.chdir("/rolldog")

salt=secrets_parser.parse("variables.txt")["SALT"]
hash=secrets_parser.parse("variables.txt")["HASH"]

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

# threading.Thread(target=regular_catcher).start()

@app.get("/")
def home():
    args=dict(request.args)
    if "key" not in args or hashlib.sha256(salt.encode()+args["key"].encode()).hexdigest()!=hash:
        return "error: invalid key"
    ss=ImageGrab.grab()
    filename="screenshots/"+str(time.time())+".png"
    ss.save(filename, "png")
    response=send_file(filename)
    response.headers["Access-Control-Allow-Origin"]="*"
    return response

@app.get("/mouse")
def move_mouse():
    args=dict(request.args)
    if "key" not in args or hashlib.sha256(salt.encode()+args["key"].encode()).hexdigest()!=hash:
        return "error: invalid key"
    try:
        import mouse
        mouse.move(args["x"], args["y"], absolute=True, duration=0)
    except:
        pass
    return Response("true", headers={"Access-Control-Allow-Origin":"*"})

@app.get("/press")
def press():
    args=dict(request.args)
    if "key" not in args or hashlib.sha256(salt.encode()+args["key"].encode()).hexdigest()!=hash:
        return "error: invalid key"
    if args["type"]=="up":
        pyautogui.keyUp(args["content"])
    else:
        pyautogui.keyDown(args["content"])
    return Response("true", headers={"Access-Control-Allow-Origin":"*"})

@app.get("/mouse_mode")
def mouse_mode():
    args=dict(request.args)
    if "key" not in args or hashlib.sha256(salt.encode()+args["key"].encode()).hexdigest()!=hash:
        return "error: invalid key"
    if args["type"]=="up":
        pyautogui.mouseUp()
    else:
        pyautogui.mouseDown()
    return Response("true", headers={"Access-Control-Allow-Origin":"*"})

app.run(host="0.0.0.0", port=7777)