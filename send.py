import requests 

TOKEN = '5812761004:AAHywnOPZkW-v5BhTtncFXo5LgO5RnvXMck'

url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'


photo_url = 'https://images.pexels.com/photos/8566472/pexels-photo-8566472.jpeg?cs=srgb&dl=pexels-kindel-media-8566472.jpg&fm=jpg'
file_id = 'AgACAgIAAxkBAAICCGRrbL9hxbdguarW9CN7dgjo9a07AAJ2yTEbCRdhS4bMNhF6MXzzAQADAgADcwADLwQ'
data = {
    'chat_id': '1258594598',
    # 'photo': photo_url
    'photo': file_id
}
requests.get(url=url, params=data)

# r = requests.get(url=f'https://api.telegram.org/bot{TOKEN}/getUpdates')
# print(r.json()['result'][-1]['message']['photo'][0]['file_id'])