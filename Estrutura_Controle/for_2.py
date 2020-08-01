palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=',')
print('FIM')


aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)



for posição, nome in enumerate(aprovados): #Aq vc esta enumerando as cadeias
    print(f'{posição +1})', nome)


dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sabado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

for letra in set('muito_legal'):#pode vir embaralhado as letras pois esta vindo em set
    print(letra)

for numero in {1, 2, 3, 4, 5}:
    print(numero)