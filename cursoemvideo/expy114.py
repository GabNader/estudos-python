import requests
url = 'https://www.youtube.com'
try:
    retorno = requests.get(url)
    if retorno.status_code == 200:
        print(f'O site {url} está acessível e funcionando corretamente.')
    else:
        print('Não foi possível acessar o site')
except requests.RequestException:
    print('Não foi possível acessar o site')


