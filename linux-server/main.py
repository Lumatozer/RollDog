import os, threading

try:
    os.system("sudo mkdir screenshots")
except:
    pass

def start_services():
    os.system("sudo -u students sudo python3 screenshotter.py")

threading.Thread(target=start_services).start()