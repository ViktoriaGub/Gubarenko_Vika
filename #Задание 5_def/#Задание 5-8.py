def find_longest_repeated_sequence():
    max = 0
    c = 1
    p = -1
    print('Введите последовательность натуральных чисел, завершающаяся числом 0')
    while True:
        n = int(input('число '))
        if n == 0:
            break
        if n == p:
            c += 1
        else:
            c = 1
        if c > max:
            max = c
        p = n
    print(max)

find_longest_repeated_sequence()