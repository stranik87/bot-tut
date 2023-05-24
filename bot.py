import requests

TOKEN = '5812761004:AAHywnOPZkW-v5BhTtncFXo5LgO5RnvXMck'

url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url=url)

print(response.json())