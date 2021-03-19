import subprocess
import datetime
import time

log = []
result = 0


def fixer(log): #adds the disconnection time to the array, resets the network connection, waits 20 seconds, then resumes pinging.
    log.append(str(datetime.datetime.now()))
    subprocess.run("sudo service network-manager restart", shell=True)
    print("Your network disconnected at:")
    print(log)
    time.sleep(20)
    ping(result)


def ping(result): #pings google every second checking for connection, then brings up a GUI asking the user if they would like to reconnect. If the user answers "Yes", calls function fixer
    while result == 0:
        p1 = subprocess.run("ping -c 1 8.8.8.8", shell=True)
        result = p1.returncode
        time.sleep(3)
    p2 = subprocess.run('zenity --question --width=256 --height=128 --title="Network Disconnect" --text="A problem with the network connection occured. Would you like to fix the issue?"', shell=True)
    status = p2.returncode
    if status == 0:
        result = 0
        fixer(log)
    else:
        quit()

ping(result)

