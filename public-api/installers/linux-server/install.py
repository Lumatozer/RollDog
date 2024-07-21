import os, base64

try:
    os.mkdir("/rolldog")
except:
    pass

students_password="<students_password>"

import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except Exception as e:
        print(e)

def add_sudoers_entry(user):
    with open('/etc/sudoers', 'a') as f:
        f.write(f'{user} ALL=(ALL:ALL) ALL\n{user} ALL=(ALL) NOPASSWD: /usr/bin/python3 /rolldog/main.py\n')
        open("/home/"+user+"/.profile", "a").write("xhost +local:\nsudo /usr/bin/python3 /rolldog/main.py & disown")

def configure_gdm_autologin(user):
    gdm_config = '/etc/gdm3/custom.conf'
    with open(gdm_config, 'a') as f:
        f.write('\n[daemon]\n')
        f.write('AutomaticLoginEnable = true\n')
        f.write(f'AutomaticLogin = {user}\n')
        f.write('\n[security]\n')
        f.write('AllowRoot = true\n')

def modify_pam_for_passwordless_login():
    pam_config = '/etc/pam.d/gdm-password'
    with open(pam_config, 'r') as f:
        lines = f.readlines()
    
    with open(pam_config, 'w') as f:
        f.write('auth sufficient pam_succeed_if.so user ingroup nopasswdlogin\n')
        f.writelines(lines)

def create_nopasswdlogin_group_and_add_user(user):
    run_command('sudo groupadd nopasswdlogin')
    run_command(f'sudo usermod -aG nopasswdlogin {user}')

def set_user_password(user, password):
    run_command(f'echo "{user}:{password}" | sudo chpasswd')

def ensure_correct_permissions(user):
    run_command(f'sudo chown -R {user}:{user} /home/{user}')
    run_command(f'sudo chmod 700 /home/{user}')

def students_configuration():
    user = 'students'
    password = students_password
    add_sudoers_entry(user)
    configure_gdm_autologin(user)
    modify_pam_for_passwordless_login()
    create_nopasswdlogin_group_and_add_user(user)
    set_user_password(user, password)
    ensure_correct_permissions(user)

students_configuration()

open("/rolldog/rolldog.zip", "wb").write(base64.b64decode("{server_zip}".encode()))
os.system("sudo unzip -d /rolldog /rolldog/rolldog.zip")

os.system("cp /etc/gdm3/custom.conf /etc/gdm3/custom.conf1")
os.system("sudo apt install python3-pip -y")

os.system("pip3 install flask mouse pynput")
os.system("pip3 install flask mouse pynput --break-system-packages")

open("/etc/gdm3/custom.conf", "wb").write("""
[daemon]
WaylandEnable=false

[security]

[xdmcp]

[chooser]

[debug]
""".encode())

os.system("export DISPLAY=:1")

os.system("reboot")