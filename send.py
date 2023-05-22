import requests 

TOKEN = '5652662088:AAFK7CrDuSOV6UJw4W3GpRT9DVKBB3iEpJQ'

url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'


photo_url = 'https://images.pexels.com/photos/8566472/pexels-photo-8566472.jpeg?cs=srgb&dl=pexels-kindel-media-8566472.jpg&fm=jpg'
data = {
    'chat_id': '1258594598',
    'photo': photo_url
}
requests.get(url=url, params=data)