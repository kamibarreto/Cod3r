#!/usr/bin/env python3
arquivo = open('/home/kami/Projetos/Cod3r/Manipulação_Arquivo/pessoas.csv') 
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()

#esse aq é o famoso stream, ele manda os dados aos poucos, diferente do primeiro
#o primeiro vc manda tudo para uma variavel, aq o python executa aos poucos