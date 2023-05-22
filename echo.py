import requests

TOKEN = '6203711973:AAGcHxZWSz5rbihY3ygUdZpMZeSMxf9qSIc'
URL   = f'https://api.telegram.org/bot{TOKEN}'


def get_last_udpate():
    url = f'{URL}/getUpdates'
    response = requests.get(url=url)

    if response.status_code == 200:
        return response.json()['result'][-1]
    

last_update = get_last_udpate()

last_update_id = last_update['update_id']

text = last_update['message']['text']
chat_id = last_update['message']['chat']['id']
print(last_update_id, chat_id, text)
