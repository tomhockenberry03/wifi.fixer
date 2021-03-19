import subprocess
import datetime
import time

log = []
result = 0


def fixer(log):
    log.append(str(datetime.datetime.now()))
    subprocess.run("sudo service network-manager restart", shell=True)
    print("Fixed")
    print(log)
    time.sleep(10)
    ping(result)


def ping(result):
    while result == 0:
        p1 = subprocess.run("ping -c 1 8.8.8.8", shell=True)
        print("Checked")
        result = p1.returncode
        print(result)
        time.sleep(1)
    p2 = subprocess.run('zenity --question --title="Network Disconnect" --text="A problem with the network connection occured. Would you like to fix the issue?"', shell=True)
    status = p2.returncode
    if status == 0:
        result = 0
        fixer(log)
    else:
        quit()

ping(result)

