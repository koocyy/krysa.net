import os
import requests
import urllib.request
import json
from colorama import Style, Fore, Back


nickname = ""
tag = ""
public_key = ""
MASTER_KEY = '$2a$10$CmT1z5R8IU3f.vQP.uitxuGo8J0nTGTGKBwZIEU89yqki62s7pwfS'
IP = ""
n = 0
t_key_dir = os.path.abspath(__file__)
key_dir = t_key_dir.strip("iwf.py") + "mykeys"

def iwantafriend():
    def get_usr_data():
        global nickname
        global tag
        global public_key
        global MASTER_KEY
        with open("usr_data.json", "r", encoding="utf-8") as read_file:
            usr_data = json.load(read_file)
            nickname = usr_data['nickname']
            tag = usr_data['tag']

        with open(f"{key_dir}/public.pem", "r") as p_key:
            public_key = p_key.read()

    # ---THE UPDATE---
    headry = {
        'X-Master-Key': MASTER_KEY
    }
    PUTheadry = {
        'Content-Type': 'application/json',
        'X-Master-Key': MASTER_KEY
    }
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    json_url = "https://api.jsonbin.io/v3/b/69139b6bae596e708f532eb8"
    req = requests.get(url=json_url, json=None, headers=headry)
    bcast_list = req.json()
    Bcast_List = bcast_list['record']
    get_usr_data()
    new_object = external_ip

    ##formating??
    #print("PUVODNI:\n" + str(Bcast_List))
    new_value = {
    'nickname': nickname,
    'tag': tag,
    'public_key': public_key
    }
    Bcast_List[new_object] = new_value
    new_json = json.dumps(Bcast_List, indent=2)
    #print("POSILAM:\n" + str(new_json))
    ##is the update alr?
    requests.put(url=json_url, data=new_json, headers=PUTheadry)
    #return print(update.status_code)

def givemeafriend():
    global IP
    json_url = "https://api.jsonbin.io/v3/b/69139b6bae596e708f532eb8"
    headry = {
        'X-Master-Key': MASTER_KEY
    }
    req = requests.get(url=json_url, json=None, headers=headry)
    F_list = req.json()
    f_list = F_list['record']
    print(Fore.LIGHTGREEN_EX + "Found " + Fore.LIGHTBLUE_EX + str(len(f_list)) + Fore.LIGHTGREEN_EX + " users who want a friend:" + Style.RESET_ALL)

    for ip, user_data in f_list.items():

        print(Fore.LIGHTMAGENTA_EX + user_data['nickname'] + Style.RESET_ALL)

    print(Fore.LIGHTYELLOW_EX + "Type the nickname of which user you want to add." + Style.RESET_ALL)
    decis_nick = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + ">> " + Style.RESET_ALL)

    for ip, user_data in f_list.items():
        if isinstance(user_data, dict) and user_data.get('nickname') == decis_nick:
            IP = str(ip)
            friend_nick = user_data['nickname']
            public__key = user_data['public_key']
            #print(f"{friend_nick}\n{public__key}")
            with open(f"{key_dir}/{friend_nick}_public_key.pem", "w") as f:
                f.write(public__key)
    print(Fore.LIGHTMAGENTA_EX + friend_nick + Fore.LIGHTGREEN_EX + " has been added to your friends list! Type " + Fore.LIGHTCYAN_EX + 'flist' + Fore.LIGHTGREEN_EX + " to show your friends list." +Style.RESET_ALL)