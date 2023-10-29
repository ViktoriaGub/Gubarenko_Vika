def print_divisors(n):
    d = []
    for i in range(1, n + 1):
        if n % i == 0:
            d.append(i)
    print("Делители числа", n, ":", end=" ")
    print(*d, sep=" ")
nu = int(input("Введите число: "))
print_divisors(nu)
