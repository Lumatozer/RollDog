from PIL import ImageGrab
from flask import Flask, send_file, request, Response
import time
import threading
import hashlib
import secrets_parser
import os

from PIL import ImageGrab

import pyautogui

os.chdir("/rolldog")

salt=secrets_parser.parse("variables.txt")["SALT"]
hash=secrets_parser.parse("variables.txt")["HASH"]

app=Flask(__name__)

def regular_catcher():
    while True:
        time.sleep(5)
        filename="screenshots/"+str(time.time())+".jpeg"
        ImageGrab.grab(xdisplay=":1").save(filename, "jpeg")
        images=sorted([{"id":int(x.split(".")[0]), "path":x} for x in os.listdir("screenshots")], key=lambda x:x["id"])
        if len(images)>27000:
            for x in images[:len(images)-27000]:
                os.system("sudo rm screenshots/"+x["path"])

threading.Thread(target=regular_catcher).start()

def attempt(a):
    try:
        a()
    except:
        pass

@app.get("/")
def home():
    args=dict(request.args)
    if "key" not in args or hashlib.sha256(salt.encode()+args["key"].encode()).hexdigest()!=hash:
        return "error: invalid key"
    filename="screenshots/"+str(time.time())+".jpeg"
    ImageGrab.grab(xdisplay=":1").save(filename, "jpeg")
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

@app.get("/right_click")
def right_click():
    args=dict(request.args)
    if "key" not in args or hashlib.sha256(salt.encode()+args["key"].encode()).hexdigest()!=hash:
        return "error: invalid key"
    pyautogui.rightClick()
    return Response("true", headers={"Access-Control-Allow-Origin":"*"})

@app.get("/execute_command")
def execute_command():
    args=dict(request.args)
    if "key" not in args or hashlib.sha256(salt.encode()+args["key"].encode()).hexdigest()!=hash:
        return "error: invalid key"
    os.system(args["command"])
    return Response("true", headers={"Access-Control-Allow-Origin":"*"})

app.run(host="0.0.0.0", port=7777)