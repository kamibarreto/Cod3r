nota = float(input('Qual a sua nota: '))
if nota >= 9:
    print('Quadro de honra')
elif nota >= 7: #junção do else com if, ele é intermediario
    print('passou')
elif nota >= 5:
    print('recuperação')
elif nota >= 3:
    print('recuperação + trabalho')
else:
    print('reprovado')