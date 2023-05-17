import requests 

TOKEN = '6203711973:AAHo-eqpnqHk0MCDLy8nLcZBfuBa5ysHAow'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

data = {
    'chat_id': 1258594598,
    'text': 'Hello World!'
}

response = requests.get(url=url, params=data)
