A = int(input("Введите значение числителя А: "))
B = int(input("Введите значение знаменателя В: "))
C = int(input("Введите значение числителя С: "))
D = int(input("Введите значение знаменателя D: "))
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def subtract_fractions(a, b, c, d):
    n = a * d - b * c
    de = b * d
    g = gcd(n, d)
    n /= g
    de /= g
    return n, de
r = subtract_fractions(A, B, C, D)
print("Результат вычитания:", r[0], "/", r[1])