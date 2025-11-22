import os
import requests
import json
from colorama import Style, Fore, Back
import rsa
from base64 import b64encode, b64decode


t_key_dir = os.path.abspath(__file__)
key_dir = t_key_dir.strip("messages.py") + "mykeys"
MASTER_KEY = '$2a$10$CmT1z5R8IU3f.vQP.uitxuGo8J0nTGTGKBwZIEU89yqki62s7pwfS'
last_message_num = ""

def send_message(nickname, message):
    global MASTER_KEY
    global last_message_num
    with open("usr_data.json", mode="r", encoding="utf-8") as read_file:
        usr_data = json.load(read_file)
        my_nickname = usr_data['nickname']
    n_message = my_nickname + ": " + message
    try:
        with open(f"{key_dir}/{nickname}_public_key.pem", "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())
        enc_message = rsa.encrypt(n_message.encode('utf-8'), public_key)

        headry = {
            'X-Master-Key': MASTER_KEY
        }
        PUTheadry = {
            'Content-Type': 'application/json',
            'X-Master-Key': MASTER_KEY
        }
        json_url = "https://api.jsonbin.io/v3/b/691a506843b1c97be9b1c553"
        req = requests.get(url=json_url, json=None, headers=headry)
        mess = req.json()
        messages = mess['record']
        with open("usr_data.json", mode="r", encoding="utf-8") as read_file:
            usr_data = json.load(read_file)
            my_nickname = usr_data['nickname']
        for users, Messages in messages.items():
            if users==nickname:
                if len(Messages)<1:
                    last_message_num = 0
                else:
                    for num, zpravy in Messages.items():
                            last_message_num = num
        my_messages = messages[nickname]
        n_object = str(int(last_message_num) + 1)
        n_val = b64encode(enc_message).decode('utf-8')
        my_messages[n_object] = n_val
        new_mess = json.dumps(messages, indent=2)
        update = requests.put(url=json_url, data=new_mess, headers=PUTheadry)
        return print(update.status_code)
    except:
        print(Fore.LIGHTRED_EX + "You dont have that user added or used a space at the end." + Style.RESET_ALL)


def get_messages_num():
    headry = {
        'X-Master-Key': MASTER_KEY
    }
    json_url = "https://api.jsonbin.io/v3/b/691a506843b1c97be9b1c553"
    req = requests.get(url=json_url, json=None, headers=headry)
    mess = req.json()
    messages = mess['record']
    my_messages = messages['k']
    def h():
        if len(my_messages)>1:
            h = "s."
            return h
        else:
            h = "."
            return h
    print(Fore.LIGHTGREEN_EX + "You have " + Fore.LIGHTBLUE_EX + str(len(my_messages)) + Fore.LIGHTGREEN_EX + f" message{h()}" + Style.RESET_ALL)

def decrypt_messages():
    with open("usr_data.json", mode="r", encoding="utf-8") as read_file:
        usr_data = json.load(read_file)
        my_nickname = usr_data['nickname']
    headry = {
        'X-Master-Key': MASTER_KEY
    }
    json_url = "https://api.jsonbin.io/v3/b/691a506843b1c97be9b1c553"
    req = requests.get(url=json_url, json=None, headers=headry)
    mess = req.json()
    messages = mess['record']
    my_messages = messages[my_nickname]
    for num, message in my_messages.items():
        print(Fore.LIGHTBLUE_EX + num + Style.RESET_ALL + "\t")
        with open(f"{key_dir}/private.pem", "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())
        message_bytes = b64decode(message)
        clear_mes = rsa.decrypt(message_bytes, private_key)
        clear_mess = clear_mes.decode('utf-8')
        print(clear_mess + "\n")