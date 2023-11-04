def print_square_numbers(n):
    i = 1
    while i**2 <= n:
        print(i**2)
        i += 1

n = int(input('Введите число: '))
print_square_numbers(n)