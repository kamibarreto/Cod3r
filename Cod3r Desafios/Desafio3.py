nota = float(input('Digite a sua nota: '))

if nota > 10:
    print('Nota invalida')
elif nota >= 9.1:
    print('Nota A')
elif nota >= 8.1:
    print('Nota A-')
elif nota >= 7.1:
    print('Nota B')
elif nota >= 6.1:
    print('Nota B-')
elif nota >= 5.1:
    print('Nota C')
elif nota >= 4.1:
    print('Nota C-')
elif nota >= 3.1:
    print('Nota D')
elif nota >= 2.1:
    print('Nota D-')
elif nota >= 1.1:
    print('Nota E')
elif nota >= 0.0:
    print('Nota E-')
else:
    print('Nota invalida')