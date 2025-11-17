#ITS ON GITHUB YAYYYY
import time
from random import randint
import urllib.request
import json
import colorama
from colorama import Fore, Style, Back
import os
from iwf import iwantafriend, givemeafriend
from keys import gen_keys
from messages import send_message, get_messages

colorama.init(autoreset=True)
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
t_key_dir = os.path.abspath(__file__)
key_dir = t_key_dir.strip("ini.py") + "/mykeys"



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
    rand = randint(0, 5)
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
        gen_keys()
        usr_data = {
            "nickname": nickname,
            "tag": randint(0, 1000)
        }
        with open("usr_data.json", mode="w", encoding="utf-8") as write_file:
            json.dump(usr_data, write_file)
        return True
    else:
        print("Neco je spatne!")
        return False

def welcome():
    with open("usr_data.json", mode="r", encoding="utf-8") as read_file:
        usr_data = json.load(read_file)
        print("Welcome " + Fore.LIGHTYELLOW_EX + usr_data['nickname'] + Style.RESET_ALL + "!")

def are_keys_generated():
    if os.path.exists(f"{key_dir}/public.pem")==True and os.path.exists(f"{key_dir}/private.pem")==True:
        return True
    else:
        gen_keys()
        print("Please restart the application!")
        return False

if isregistered():
    if are_keys_generated():
        welcome()
        get_messages()
    else:
        quit()


while isregistered():
    current_cmd = input(Style.BRIGHT + Fore.LIGHTGREEN_EX + ">> " + Style.RESET_ALL)
    if current_cmd=="help" or current_cmd=="?" or current_cmd=="h":
        print(Fore.LIGHTGREEN_EX + "x / exit" + Style.RESET_ALL + " -- Exits.\n" + Fore.LIGHTGREEN_EX + "help / ? / h" + Style.RESET_ALL + " -- Shows this help info.")
        print(Fore.LIGHTGREEN_EX + "ip / myip" + Style.RESET_ALL + " -- Shows your current public IP adress.")


    elif current_cmd=="ip" or current_cmd=="myip":
        print(Style.DIM + randBcolor() + randFcolor() + external_ip + Style.RESET_ALL)


    elif current_cmd=="iwantafriend" or current_cmd=="iwf":
        print(Fore.LIGHTGREEN_EX + "Adding you to looking-for-friends list..." + Style.RESET_ALL)
        iwantafriend()
        print(Fore.LIGHTGREEN_EX + "Getting other users who want a friend..." + Style.RESET_ALL)
        givemeafriend()


    elif current_cmd=="send" or current_cmd=="snd":
        who = input(Fore.LIGHTYELLOW_EX + "To who? >> " + Style.RESET_ALL)
        what = input(Fore.LIGHTYELLOW_EX + "And what >> " + Style.RESET_ALL)
        send_message(who, what)


    elif current_cmd=="exit" or current_cmd=="x":
        print(Fore.LIGHTRED_EX + "Exiting...")
        break

    elif current_cmd=="clear":
        print("\n"*100)


    else:
        r = randint(50,100)
        if r==67:
            print(Fore.LIGHTMAGENTA_EX + "\\O/ i dunno this one gng" + Style.RESET_ALL)
        else:
            print("Unknown command! Use " + Fore.LIGHTGREEN_EX +  "help" + Style.RESET_ALL + ", " + Fore.LIGHTGREEN_EX +  "h" + Style.RESET_ALL +" or " + Fore.LIGHTGREEN_EX +  "?" + Style.RESET_ALL +" for help. ")