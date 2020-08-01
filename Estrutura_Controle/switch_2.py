def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexto',
        7: 'Sabado',
    }
    return dias.get(dia, "**Fora Do Sistema**")

if __name__ == '__main__':
    for dia in range(1, 8):
        if 2 <= dia <= 6:
            print(f'{dia}: {get_dia_semana(dia)} é meio de semana')
        elif dia == 7:
            print(f'{dia}: {get_dia_semana(dia)} é fim de semana')
        elif dia == 1:
            print(f'{dia}: {get_dia_semana(dia)} é fim de semana')
        else:
            print('invalido')
