import requests


TOKEN = '5812761004:AAEm91-oifYmq1Z9CzQIL7vkrN5VUrEGfB8'
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
        'chat_id': chat_id,
        'photo': photo_id
    }
    requests.get(url=url, params=data)


def send_sticker(chat_id, sticker):
    url = f'{URL}/sendSticker'
    data = {
        'chat_id': chat_id,
        'sticker': sticker
    }
    requests.get(url=url, params=data)
    
def send_video(chat_id,video):
    url = f'{URL}/sendVideo'
    data = {
        'chat_id':chat_id,
        'video':video
    }
    requests.get(url=url,params=data)
    
def send_audio(chat_id,audio):
    url = f'{URL}/sendAudio'
    data = {
        'chat_id':chat_id,
        'audio':audio
    }
    requests.get(url=url,params=data)
    
def send_document(chat_id,document):
    url = f'{URL}/sendDocument'
    data = {
        'chat_id':chat_id,
        'document':document
    }
    requests.get(url=url,params=data)
    
def send_voice(chat_id,voice):
    url = f'{URL}/sendVoice'
    data = {
        'chat_id':chat_id,
        'voice':voice
    }
    requests.get(url=url,params=data)
    
def send_location(chat_id,latitude,longitude):
    url = f'{URL}/sendLocation'
    data = {
        'chat_id':chat_id,
        'latitude':latitude,
        'longitude':longitude
    }
    requests.get(url=url,params=data)
    
def send_contact(chat_id,phone_number,first_name):
    url = f'{URL}/sendContact'
    data = {
        'chat_id':chat_id,
        'phone_number':phone_number,
        'first_name':first_name
    }
    requests.get(url=url,params=data)
    
def send_dice(chat_id,emoji=''):
    url = f'{URL}/sendDice'
    data = {
        'chat_id':chat_id,
        
    }