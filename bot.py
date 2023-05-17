import requests

response = requests.get('https://api.telegram.org/bot6203711973:AAHo-eqpnqHk0MCDLy8nLcZBfuBa5ysHAow/getMe')

print(response.json())