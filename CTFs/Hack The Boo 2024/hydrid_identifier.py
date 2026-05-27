import requests

URL = 'http://localhost:1337'
r = requests.post(f'{URL}/a-cool-endpoint', json={'key1': 'json', 'key2': 'data'})

print(r.content)
