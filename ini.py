#ITS ON GITHUB YAYYYY
import time
from random import randint
import urllib.request
import json
import colorama
from colorama import Fore, Style, Back
import os

colorama.init(autoreset=True)
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')


def randFcolor():
    rand = randint(0, 6)
    colors = [
        Fore.LIGHTRED_EX,
        Fore.LIGHTGREEN_EX,
        Fore.LIGHTYELLOW_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTMAGENTA_EX,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTWHITE_EX
    ]
    return colors[rand]

def randBcolor():
    rand = randint(0, 6)
    colors = [
        Back.LIGHTRED_EX,
        Back.LIGHTGREEN_EX,
        Back.LIGHTYELLOW_EX,
        Back.LIGHTBLUE_EX,
        Back.LIGHTMAGENTA_EX,
        Back.LIGHTCYAN_EX,
    ]
    return colors[rand]

def isregistered():
    is_he = os.path.exists("usr_data.json")
    if is_he==True:
        return True
    elif is_he==False:
        nickname = input("nickname" + randFcolor() + " --> " + Style.RESET_ALL)
        usr_data = {
            "nickname": nickname,
            "tag": randint(0, 1000)
        }
        with open("usr_data.json", mode="w", encoding="utf-8") as write_file:
            json.dump(usr_data, write_file)
        print("Welcome " + Fore.LIGHTYELLOW_EX + nickname + Style.RESET_ALL + "!")
        return True
    else:
        print("Neco je spatne!")
        return False

def welcome():
    with open("usr_data.json", mode="r", encoding="utf-8") as read_file:
        usr_data = json.load(read_file)
        print("Welcome " + Fore.LIGHTYELLOW_EX + usr_data['nickname'] + Style.RESET_ALL + "!")

if isregistered():
    welcome()

while isregistered():
    current_cmd = input(Style.BRIGHT + Fore.LIGHTGREEN_EX + ">> " + Style.RESET_ALL)
    if current_cmd=="help" or current_cmd=="?" or current_cmd=="h":
        print(Fore.LIGHTGREEN_EX + "x / exit" + Style.RESET_ALL + " -- Exits.\n" + Fore.LIGHTGREEN_EX + "help / ? / h" + Style.RESET_ALL + " -- Shows this help info.")
        print(Fore.LIGHTGREEN_EX + "ip / myip" + Style.RESET_ALL + " -- Shows your current public IP adress.")


    elif current_cmd=="ip" or current_cmd=="myip":
        print(Style.DIM + randBcolor() + randFcolor() + external_ip + Style.RESET_ALL)


    elif current_cmd=="mkfriend" or current_cmd=="getafriend":
        print(Fore.LIGHTGREEN_EX + "Starting getafriend protocol..." + Style.RESET_ALL)
        open("broadcast.py")


    elif current_cmd=="exit" or current_cmd=="x":
        print(Fore.LIGHTRED_EX + "Exiting...")
        time.sleep(1.5)
        break


    else:
        r = randint(50,100)
        if r==67:
            print(Fore.LIGHTMAGENTA_EX + "\\O/ i dunno this one gng" + Style.RESET_ALL)
        else:
            print("Unknown command! Use " + Fore.LIGHTGREEN_EX +  "help" + Style.RESET_ALL + ", " + Fore.LIGHTGREEN_EX +  "h" + Style.RESET_ALL +" or " + Fore.LIGHTGREEN_EX +  "?" + Style.RESET_ALL +" for help. ")