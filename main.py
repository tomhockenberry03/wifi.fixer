import subprocess
import datetime
import time
log = []
result = 0

def fixer(log):
    global log
    global result
    log.append(str(datetime.datetime.now()))
    subprocess.run("sudo service network-manager restart", shell=True)

def ping(result):
    global result
    global log
    while result == 0:
        p1 = subprocess.run("ping -c 1 8.8.8.8", shell=True)
        result = p1.returncode
        time.sleep(3)
    fixer(log)

ping(result)

