trabalho_na_terça = input('Digite False ou True: ')
trabalho_na_quarta = input('Digite False ou True: ')
tv_50 = trabalho_na_terça and trabalho_na_quarta
#Os dois trabalhos devem dar certo para obter a de 50
sorvete = trabalho_na_terça or trabalho_na_quarta
#O trabalho de terça OU (or) trabalho de quarta dando certo, ele compra a tv
tv_30 = trabalho_na_terça != trabalho_na_quarta #Xor
# ele compra a tv se  apenas um, e apenas um trabalho for realizado, ou seja um "ou" exclusivo, seria o operador do xor, porem não tem, então usa o diferente
saudavel = not sorvete
# ele vai tomar sorvete se nenhum dos dois trabalhos dar certo, negar o sorvete
print('Tv 50: {} / sorvete: {} / Tv 30: {} / saudavel: {}'.format(tv_50, sorvete, tv_30, saudavel))