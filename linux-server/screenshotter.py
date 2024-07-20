from PIL import ImageGrab
from flask import Flask, send_file, request, Response
import time
import threading
import hashlib
import secrets_parser
import os
import subprocess

import pyautogui
import logging

logging.basicConfig(level=logging.ERROR,
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

os.chdir("/rolldog")

salt=secrets_parser.parse("variables.txt")["SALT"]
hash=secrets_parser.parse("variables.txt")["HASH"]

app=Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(e):
    # log the exception
    logging.exception('Exception occurred')
    # return a custom error page or message
    return "server error", 500

def regular_catcher():
    while True:
        time.sleep(5)
        os.system("sudo scrot "+"screenshots/"+str(int(time.time()))+".png")
        images=sorted([{"id":int(x.split(".")[0]), "path":x} for x in os.listdir("screenshots")], key=lambda x:x["id"])
        if len(images)>27000:
            for x in images[:len(images)-27000]:
                os.system("sudo rm screenshots/"+x["path"])

# threading.Thread(target=regular_catcher).start()

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
    filename="screenshots/"+str(time.time())+".png"
    data=""
    try:
        from PIL import ImageGrab
        attempt(lambda:ImageGrab.grab(xdisplay="0").save(filename, "png"))
        attempt(lambda:ImageGrab.grab(xdisplay="1").save(filename, "png"))
        attempt(lambda:ImageGrab.grab(xdisplay=":0").save(filename, "png"))
        attempt(lambda:ImageGrab.grab(xdisplay=":1").save(filename, "png"))
        attempt(lambda:os.system("xwd -root -out /tmp/hi.xwd"))
        ImageGrab.grab(xdisplay=":1").save(filename, "png")
    except Exception as e:
        logging.exception("Exception:\n"+str(e))
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