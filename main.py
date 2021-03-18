import subprocess
import datetime

p1 = subprocess.run("ping -c 1 8.8.8.8", shell=True)
result = p1.returncode


if result != 0:
    subprocess.run("sudo service network-manager restart", shell=True)

log=[]
log.append(str(datetime.datetime.now()))

