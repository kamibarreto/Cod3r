#!/usr/bin/env python3
arquivo = open('/home/kami/Projetos/Cod3r/Manipulação_Arquivo/pessoas.csv') #ele vai abrir o arquivo pessoas.csv com o "open"
dados = arquivo.read() #read vai colocar o conteudo de arquivo em dados, e ai ele vai poder fechar arquivo, pq tudo vai estar na variavel
arquivo.close()

for registro in dados.splitlines(): #ele vai pegar uma das linhas dos nomes e idade e separar
    #print(*registro.split(','))
    print('Nome: {}\n Idade: {}'.format(*registro.split(',')))
