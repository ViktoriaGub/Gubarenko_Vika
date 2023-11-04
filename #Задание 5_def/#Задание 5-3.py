def calculate():
    N = int(input('Введите число: '))
    a = 0
    b = 1
    while b  <=  N:
        a += 1
        b *= 2
    a -= 1
    b //= 2
    return a, b
power, result = calculate()
print(power, result)