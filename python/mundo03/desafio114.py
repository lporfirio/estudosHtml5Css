'''
Crie um código em python que teste se o site 'Pudim' está acessivel no computador usado



import requests

url = "http://www.pudim.com.br"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print('Site acessível')
except:
    print('Site inacessível')

'''

import requests

url = "http://www.pudim.com.br"
try:
    response = requests.get(url)
    response.raise_for_status()
except:
    print(f"O site {url} está inacessível.")
else:
    print(f"O site {url} está acessível!")
    