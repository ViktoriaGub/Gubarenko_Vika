def calculate_days():
    x = float(input('Введите сколько км пробежал спортсмен в 1 день '))
    y = float(input('Введите y километров '))
    a = 1
    di = x
    while di < y:
        di += di * 0.1
        a += 1
    print(a)
calculate_days()    