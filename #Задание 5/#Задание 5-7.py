c = 0
p = -1
print('Введите последовательность которая состоит из натуральных чисел и завершается числом 0  ')
while True:
    n = int(input(' '))
    if n == 0:
        break
    if n > p:
        c += 1
    p = n
print(c)