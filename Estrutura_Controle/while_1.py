from random import randint #gera um valor aleatorio entre o numero que esta entre ()

numero_informado = -1 #ele colocou o menos -1 pq esta fora possibilidade entre 0 a 9
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto: #enquanto o numero informado for diferente do numero secreto, vai continuar tentando, no caso o usuario
    numero_informado = int(input('Informe o numero: '))

print('Numero secreto {} foi encontrado!'.format(numero_secreto))


#aq é um laço indefinido, ou seja bem aleatorio, porem se tentar ficar executando o mesmo numero não vai dar
#usado em casos especificos 
#https://www.youtube.com/watch?v=9Xzrzmq3eDg