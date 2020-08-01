#!/usr/bin/env python3
arquivo = open('/home/kami/Projetos/Cod3r/Manipulação_Arquivo/pessoas.csv') 
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()

#strip tirou os espaços, lembre-se boco, vc estudou