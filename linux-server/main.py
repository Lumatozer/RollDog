import os, threading

try:
    os.system("sudo mkdir /rolldog/screenshots")
except:
    pass

def start_services():
    os.system("python3 /rolldog/screenshotter.py")

threading.Thread(target=start_services).start()