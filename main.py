import subprocess

#tests network connection by pinging google
#if wifi is down, it will return the error "network is unreachable"
subprocess.run("ping -c 1 8.8.8.8", shell=True)


subprocess.run("sudo service network-manager restart") #restarts the internet
