import requests

response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')

text = response.content.decode('cp1251')

with open('./vocab/russian.txt', 'wb') as ru:
    ru.write(text.encode('utf-8'))

with open('./vocab/russian.txt', encoding = 'utf-8', mode = 'r') as ru:
    vocab = [word.rstrip() for word in ru]