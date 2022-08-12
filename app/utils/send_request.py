import requests
from config import *
import json

class Main:
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json',
        'Authorization': TOKEN 
    }

    url = 'https://probe.fbrq.cloud/v1/{}'


def send_message(data, msg_id):
    url = Main.url.format(
        'send/{}'.format(msg_id)
    )

    response = requests.post(
        url, 
        json=data,
        headers=Main.headers
    )
    if response.status_code == 200:
        return True
    else:
        return False
