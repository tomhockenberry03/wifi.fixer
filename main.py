import os

#tests network connection by pinging google
#if wifi is down, it will return the error "network is unreachable"
os.system("ping -c 1 8.8.8.8")


os.system("sudo service network-manager restart") #restarts the internet
