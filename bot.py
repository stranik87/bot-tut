import requests

TOKEN = '6203711973:AAHo-eqpnqHk0MCDLy8nLcZBfuBa5ysHAow'

url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url=url)

print(response.json())