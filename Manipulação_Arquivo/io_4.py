#!/usr/bin/env python3

try:
    arquivo = open('/home/kami/Projetos/Cod3r/Manipulação_Arquivo/pessoas.csv') 

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
        
finally:
    print('finally')
    arquivo.close()

#mesmo se der erro ou acerto no try 'o bloco', ele vai passar pelo finally, ou seja, oq tiver no finally, vai ser executado


if arquivo.closed:
    print('Arquivo ja foi fechado')