import requests
import json

token = "567333dfb32fdc80-e7890a5e0966fc9a-81a92bb42db4f3c6"
# super_admin_id =


def set_web_hook():
    url = "https://chatapi.viber.com/pa/set_webhook"

    payload = {
        "url": "https://www.broadwayinfosis.com",
        "auth_token": token
    }

    headers = {
        "Content-Type": "application/json"
    }

    r = requests.post(url=url, data=json.dumps(payload), headers=headers)

    print("Set Webhook Response:")
    print(r.status_code)
    print(r.json())


def get_account_info():
    url = "https://chatapi.viber.com/pa/get_account_info"

    payload = {
        "auth_token": token
    }

    headers = {
        "Content-Type": "application/json"
    }

    r = requests.post(url=url, data=json.dumps(payload), headers=headers)

    print("Get Account Info Response:")
    print(r.status_code)
    print(r.json())


set_web_hook()
get_account_info()