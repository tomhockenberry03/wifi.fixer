import subprocess
import datetime
import time

log = []
result = 0


def fixer(log):
    log.append(str(datetime.datetime.now()))
    subprocess.run("sudo service network-manager restart", shell=True)
    print("Fixed")
    time.sleep(10)
    ping(result)


def ping(result):
    print(result)
    while result == 0:
        p1 = subprocess.run("ping -c 1 8.8.8.8", shell=True)
        print("Checked")
        result = p1.returncode
        print(result)
        time.sleep(1)
    result = 0
    fixer(log)

ping(result)

