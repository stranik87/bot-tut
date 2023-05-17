import requests

TOKEN = '6203711973:AAHo-eqpnqHk0MCDLy8nLcZBfuBa5ysHAow'

url = f'https://api.telegram.org/bot{TOKEN}/getMe'

response = requests.get()

print(response.json())