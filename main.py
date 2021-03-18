import subprocess
import datetime

def fix_and_continue(result):
    if result != 0:
        subprocess.run("sudo service network-manager restart", shell=True)
        log = []
        log.append(str(datetime.datetime.now()))
    ping()

def ping():
    result = 0
    while result == 0:
        p1 = subprocess.run("ping -c 1 8.8.8.8", shell=True)
        result = p1.returncode
    fix_and_continue(result)

ping()


