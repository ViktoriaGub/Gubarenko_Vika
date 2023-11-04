def count_numbers():
    b = 1
    c = 0
    while True:
        n = int(input('Введите число '))
        if n == 0:
            break
        c += 1
    print(c)
count_numbers()