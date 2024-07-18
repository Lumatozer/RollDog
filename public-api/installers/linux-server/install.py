import os, base64

try:
    os.mkdir("/rolldog")
except:
    pass

open("/rolldog/rolldog.zip", "wb").write(base64.b64decode("{server_zip}".encode()))
os.system("sudo unzip -d /rolldog /rolldog/rolldog.zip")

os.system("cp /etc/gdm3/custom.conf /etc/gdm3/custom.conf1")
os.system("sudo apt install python3-pip -y")

os.system("pip3 install flask mouse pyautogui")
os.system("pip3 install flask mouse pyautogui --break-system-packages")

open("/etc/gdm3/custom.conf", "wb").write("""
[daemon]
WaylandEnable=false

[security]

[xdmcp]

[chooser]

[debug]
""".encode())

os.system("export DISPLAY=:1")

open("/etc/systemd/system/rolldog.service", "wb").write(b"""
[Unit]
Description=Rolldog
After=network.target

[Service]
User=root
Type=simple
WorkingDirectory=/rolldog
Environment="DISPLAY=:1"
ExecStartPre=/usr/bin/xhost +SI:localuser:teachers
ExecStartPre=/usr/bin/xhost +SI:localuser:root
ExecStart=sudo -u teachers python3 /rolldog/main.py
Restart=always

[Install]
WantedBy=multi-user.target
"""[1:-1])
os.system("sudo systemctl daemon-reload")
os.system("sudo systemctl enable rolldog.service")
os.system("sudo systemctl start rolldog service")
os.system("sudo systemctl status rolldog.service")