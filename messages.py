import os
import requests
import urllib.request
import json
from colorama import Style, Fore, Back
import rsa

t_key_dir = os.path.abspath(__file__)
key_dir = t_key_dir.strip("messages.py") + "mykeys"
MASTER_KEY = '$2a$10$CmT1z5R8IU3f.vQP.uitxuGo8J0nTGTGKBwZIEU89yqki62s7pwfS'

def send_message(nickname, message):
    global MASTER_KEY

    try:
        with open(f"{key_dir}/{nickname}_public_key.pem", "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())
        enc_message = rsa.encrypt(message.encode(), public_key)

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
        print(str(messages) + "\n-----------------\n")
        n_object = nickname
        n_val = str(enc_message)
        messages[n_object] = n_val
        new_mess = json.dumps(messages, indent=2)
        print(new_mess)
        update = requests.put(url=json_url, data=new_mess, headers=PUTheadry)
        return print(update.status_code)
    except:
        print(Fore.LIGHTRED_EX + "You dont have that user added or used a space at the end." + Style.RESET_ALL)


def get_messages():
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


    ''' with open(f"{key_dir}/private.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    clear_mes = rsa.decrypt(enc_message, private_key)
    clear_mess = str(clear_mes)
    print(clear_mess.strip("b'"))
    '''