peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Condição: Magreza')
elif  imc < 24.9:
    print('Condição: normal')
elif imc < 30:
    print('Condição: Sobre peso')
else:
    print('Condição: Obeso')

print('Seu IMC é igual á: {}'.format(imc))