import os, threading

try:
    os.system("sudo mkdir screenshots")
    os.system("sudo -u students xhost +local:students")
except:
    pass

def start_services():
    os.system("sudo -u students python3 screenshotter.py")

threading.Thread(target=start_services).start()