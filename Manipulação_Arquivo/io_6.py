#!/usr/bin/env python3

with open('/home/kami/Projetos/Cod3r/Manipulação_Arquivo/pessoas.csv') as arquivo:
    with open('/home/kami/Projetos/Cod3r/Manipulação_Arquivo/pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)
        
if arquivo.closed:
    print('Arquivo ja foi fechado')

if saida.closed:
    print('O arquivo de saida foi fechado')

#nesse codigo, ele leu o arquivo e fez um novo, no caso o txt
    