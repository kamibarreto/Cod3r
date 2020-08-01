def get_dia_semana(dia):
    dias = {
        1: 'Domingo', #esse 1: é o dia, ou seja, o dicionario
        2: 'segunda',
        3: 'terça',
        4: 'quarta',
        5: 'quinta',
        6: 'sexta',
        7: 'sabado',
    }
    return dias.get(dia, '**invalido**') #com a função "get" vc puxa a numeração dos dias, ou seja, o dicionario


if __name__ == '__main__':
    for dia in range (0, 9):
        print(f'{dia}: {get_dia_semana(dia)}')
