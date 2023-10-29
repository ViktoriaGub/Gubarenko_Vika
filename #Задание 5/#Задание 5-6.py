s = 0
c = 0
while True:
    n = int(input('Введите число '))
    if n == 0:
        break
    s += n
    c += 1
a = s / c
print(a)