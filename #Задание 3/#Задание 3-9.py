def сhocolate():
    n = int(input("Введите количество долек в ряде"))
    m = int(input("Введите количество долек в столбике"))
    k = int(input("Введите кол-во долек"))
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        print('ДА')
    else:
        print('НЕТ')
сhocolate()