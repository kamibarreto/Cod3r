import csv

from urllib import request

def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados =  entrada.read().decode('latin1')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')

if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')


#importamos o csv, e request para acessar o url e baixar
#usamos o read para ler o aquivo e usamos o decode para ler no formato desejado (latin1)
# O RESTO É SO LER O CODIGO