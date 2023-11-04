def count_increasing_sequence():
    c = 0
    p = -1
    print('Введите последовательность, которая состоит из натуральных чисел и завершается числом 0')
    while True:
        n = int(input('Введите число'))
        if n == 0:
            break
        if n > p:
            c += 1
        p = n
    print(c)
count_increasing_sequence()  