import requests

from config import TOKEN

BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def get_me():
    get_url = f"{BASE_URL}/GetMe"

    response = requests.get(get_url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Telegram serveri xatolik qaytardi!")

print(get_me())