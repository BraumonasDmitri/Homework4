def sal():
    try:
        time = float(input('Выработка в часах: '))
        salary = int(input('Ставка/час: '))
        bonus = int(input('Размер премии: '))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника составляет:  {res}.')
    except ValueError:
        return print('Необходимо ввести число!')
sal()