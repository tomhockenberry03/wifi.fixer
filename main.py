

import os


os.system("cat < /dev/null > /dev/tcp/8.8.8.8/53; echo $?") #tests network connection

os.system("sudo service network-manager restart") #restarts the internet
