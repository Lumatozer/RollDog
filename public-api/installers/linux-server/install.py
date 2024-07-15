import os

# Disable Wayland

os.system("cp /etc/gdm3/custom.conf /etc/gdm3/custom.conf1")

open("/etc/gdm3/custom.conf", "wb").write("""
[daemon]
WaylandEnable=false

[security]

[xdmcp]

[chooser]

[debug]
""".encode())

os.system("export DISPLAY=:1")

