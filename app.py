import requests

url = 'https://ru.wikipedia.org/wiki/Заглавная_страница'
response = requests.get(url)
favicon_url = response.url + '/favicon.ico'

with open('favicon.ico', 'wb') as f:
    f.write(requests.get(favicon_url).content)

print('Favicon downloaded!')
