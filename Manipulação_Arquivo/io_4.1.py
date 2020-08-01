#!/usr/bin/env python3

try:
    arquivo = open('/home/kami/Projetos/Cod3r/Manipulação_Arquivo/pessoas.csv') 

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(registro.strip().split(',')))
except IndexError: #se tiver o erro, ele vai para o proximo
    pass #no caso o finally e o if, magora se não teve erro, ele vai passar tudo normal
    #o pass serve para definir um bloco vazio, ou seja, não mostra nada      

finally:
    print('finally')
    arquivo.close()

#mesmo se der erro ou acerto no try 'o bloco', ele vai passar pelo finally, ou seja, oq tiver no finally, vai ser executado


if arquivo.closed:
    print('Arquivo ja foi fechado')