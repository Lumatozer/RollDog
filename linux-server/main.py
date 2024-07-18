import os, threading

try:
    os.system("sudo mkdir /rolldog/screenshots")
    os.system("sudo -u students xhost +local:students")
except:
    pass

def start_services():
    os.system("sudo -u students sudo python3 /rolldog/screenshotter.py")

threading.Thread(target=start_services).start()