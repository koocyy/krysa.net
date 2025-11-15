import os
import requests
import urllib.request
import json


nickname = ""
tag = ""
public_key = ""

t_key_dir = os.path.abspath(__file__)
key_dir = t_key_dir.strip("iwf.py") + "/mykeys"

def iwantafriend():
    def get_usr_data():
        global nickname
        global tag
        global public_key
        with open("usr_data.json", "r", encoding="utf-8") as read_file:
            usr_data = json.load(read_file)
            nickname = usr_data['nickname']
            tag = usr_data['tag']

        with open(f"{key_dir}/public.pem", "r") as p_key:
            public_key = p_key.read()

    # ---THE UPDATE---
    MASTER_KEY = '$2a$10$CmT1z5R8IU3f.vQP.uitxuGo8J0nTGTGKBwZIEU89yqki62s7pwfS'
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

    #formating??
    print("PUVODNI:\n" + str(Bcast_List))
    new_value = {
    'nickname': nickname,
    'tag': tag,
    'public_key': public_key
    }
    Bcast_List[new_object] = new_value
    new_json = json.dumps(Bcast_List, indent=2)
    print("POSILAM:\n" + str(new_json))
    #is the update alr?
    update = requests.put(url=json_url, data=new_json, headers=PUTheadry)
    print(update.status_code)


