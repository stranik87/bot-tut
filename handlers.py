import requests


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


def send_photo(chat_id, photo_id):
    url = f'{URL}/sendPhoto'
    data = {
        'chat_id': '1258594598',
        'photo': photo_id
    }
    requests.get(url=url, params=data)


def send_sticker(chat_id, sticker):
    url = f'{URL}/sendSticker'
    data = {
        'chat_id': '1258594598',
        'sticker': sticker
    }
    requests.get(url=url, params=data)
