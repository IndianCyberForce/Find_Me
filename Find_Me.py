import requests
import os
from time import sleep
from colorama import Fore
#Author Mr.Grey_Hacker 
os.system('clear')
banner = """
 ███████████ █████ ██████   █████ ██████████      ██████   ██████ ██████████
░░███░░░░░░█░░███ ░░██████ ░░███ ░░███░░░░███    ░░██████ ██████ ░░███░░░░░█
 ░███   █ ░  ░███  ░███░███ ░███  ░███   ░░███    ░███░█████░███  ░███  █ ░ 
 ░███████    ░███  ░███░░███░███  ░███    ░███    ░███░░███ ░███  ░██████   
 ░███░░░█    ░███  ░███ ░░██████  ░███    ░███    ░███ ░░░  ░███  ░███░░█   
 ░███  ░     ░███  ░███  ░░█████  ░███    ███     ░███      ░███  ░███ ░   █
 █████       █████ █████  ░░█████ ██████████      █████     █████ ██████████
░░░░░       ░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░░      ░░░░░     ░░░░░ ░░░░░░░░░░ 
"""                                                                           
print(Fore.CYAN+banner)
print(Fore.BLUE+"Author:Mr.Grey_Hacker",Fore.LIGHTYELLOW_EX+"                                          Version:1.7")                                                                           
print(Fore.GREEN+"Facebook Page:https://www.facebook.com/mrgreyhacker")
print(Fore.GREEN+"Telegram Channel:https://t.me/INDIAN_CYBER_NINJA\n")                                                                            

def Find():
    while True:
        IP=input(Fore.WHITE+"Enter Your Targate IP: ")
        nayak = requests.get("http://ip-api.com/json/"+IP).json()
        print("\n")
        print(Fore.CYAN+"GET INFORMATION")
        print(Fore.BLUE+"[+]Targate IP: "+nayak['query'])
        print("[+]Status: "+nayak['status'])
        print("[+]Country: "+nayak['country'])
        print("[+]Country Code: "+nayak['countryCode'])
        print("[+]Region: "+nayak['region'])
        print("[+]State: "+nayak['regionName'])
        print("[+]City: "+nayak['city'])
        print("[+]Lat And Lon",nayak['lat'],nayak['lon'])
        print("[+]TimeZone: "+nayak['timezone'])
        print("[+]ISP: "+nayak['isp'])
        print("[+]Industries: "+nayak['as'])
        sleep(3)
        Me()         
def Me():
        S = input(str(Fore.RED+"\nLet's Do Next IP Informatio Gather[Y/n]: "))
        if S == 'y' or S == 'Y':
            print(Fore.GREEN+banner)
            Find()
        elif S == 'N' or S == 'n':
            os.system('clear')
            print(Fore.LIGHTGREEN_EX+"Exiting")
            sleep(1)
            print(Fore.RED+banner)
            print(Fore.CYAN+"Thank's For Using ICN Tool")
            print(Fore.YELLOW+"Author: Mr.Grey_Hacker")
            exit()                
        else:
            print(Fore.RED+"\nEnter Right Option   [Invalid Option!!!]")
            Me()
Find()
