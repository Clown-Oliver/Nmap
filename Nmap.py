import os
ggyt=('''marshal\ngeoip\nuuid\nsubprocess\nurllib.request\nre\nrequests\ndatetime\nrandom\nsocket\ntime\nsys\npyfiglet\nurllib.parse''')
os.system('rm -rif req.txt')
info_file = open('req.txt' ,'a') 
write_info = open('req.txt' ,'a') 
my_info = (ggyt)
write_info.writelines(my_info)
try:
	import random,pyfiglet,sys,time,socket,requests,re,subprocess,urllib.request,uuid,marshal
	from datetime import datetime
	import requests as re
	from geoip import geolite2
	from requests import get
	from urllib.parse import unquote
except ImportError:
	print('\033[2;32mWait Pro ....')
	os.system('pip3 install -r req.txt')
	os.system('clear')
	os.system('rm -rif req.txt')
	print('\033[2;36mDownload Done ..!')
	time.sleep(3)
C = '\033[2;35m'
Xx = '\033[2;36m'
F = '\033[2;32m'
X = '\033[1;33m'
Z = '\033[1;31m'
r="\x1b[91m"
g="\x1b[92m"
ye="\x1b[93m"
w="\x1b[97m"
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system('clear')
os.system('rm -rif req.txt')
os.system("clear")
SSS = pyfiglet.figlet_format('*OlveTool*')
subprocess.call('clear', shell=True)
remoteServer    =input(F+"Enter a remote host to scan==> "+Z)
os.system("clear")
remoteServerIP  = socket.gethostbyname(remoteServer)
print (F+"-" * 60)
print ("\033[2;32mPlease wait, scanning remote host",Z+remoteServerIP)
print (F+"-" * 60)
t1 = datetime.now()
try:
    for port in range(1,65535):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("\033[2;32mPort \033[1;31m{}\033[2;32m: 	 \033[2;32mOpen".format(port))
        sock.close()
except KeyboardInterrupt:
    print (X+"You pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print ('\033[1;31mHostname could not be resolved. Exiting')
    sys.exit()
except socket.error:
    print ("\033[1;31mCouldn't connect to server")
    sys.exit()
t2 = datetime.now()
total =  t2 - t1
print ('\033[1;33mScanning Completed in: ', total)
#OliverTeam
