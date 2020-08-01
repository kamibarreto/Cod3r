#!/usr/bin/env python3

with open('/home/kami/Projetos/Cod3r/Manipulação_Arquivo/pessoas.csv') as arquivo:
    #o with(com) ele vai chamar o arquivo, e o "as" é como definir uma varivael, vc deifinou ele como arquivo
    #ele é garantido que o recurso do bloco será fechado, não precisa pedir para fechar
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
        
if arquivo.closed:
    print('Arquivo ja foi fechado')