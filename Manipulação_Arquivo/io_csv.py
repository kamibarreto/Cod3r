import csv 

with open('/home/kami/Projetos/Cod3r/Manipulação_Arquivo/pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada): #ele sabe que é um arquivo de leitura, então vc Lẽ ele
        print('Nome: {}. Idade: {}'.format(*pessoa))