import requests
import time

TOKEN = '5652662088:AAFK7CrDuSOV6UJw4W3GpRT9DVKBB3iEpJQ'
URL   = f'https://api.telegram.org/bot{TOKEN}'


def get_last_udpate():
    url = f'{URL}/getUpdates'
    response = requests.get(url=url)

    if response.status_code == 200:
        return response.json()['result'][-1]


def send_text(chat_id, text='salom, botimiga hush kelibsiz!'):
    url = f'{URL}/sendMessage'
    payload ={
        'chat_id': chat_id,
        'text': text
    }
    requests.get(url, params=payload)


last_update = get_last_udpate()
last_update_id = last_update['update_id']

while True:
    current_update = get_last_udpate()
    current_update_id = current_update['update_id']

    if last_update_id != current_update_id:
        if 'text' in current_update['message']:
            text    = current_update['message']['text']
            chat_id = current_update['message']['chat']['id']
            if text == '/start':
                send_text(chat_id=chat_id)
            else:
                send_text(chat_id=chat_id, text=text)
                
            print(current_update_id, chat_id, text)

        last_update_id = current_update_id

        time.sleep(2)