import subprocess
import datetime
#defines p1 as the process of pinging google
#for this process, -c 1 means ping it once, and 8.8.8.8 is the IP address of google.
#in order to include multiple arguments, we need the shell=True.
p1 = subprocess.run("ping -c 1 8.8.8.8", shell=True)

#for a subprocess, it has a "returncode" that is a number indicating how many errors occur during the process.
#defined result as the return code of process p1.
result = p1.returncode

#if the the return code doesn't equal 0, meaning an error occured, reset the internet

if result != 0:
    subprocess.run("sudo service network-manager restart", shell=True)

log=[]
log.append(str(datetime.datetime.now()))

