def find_negative_pairs(n):
    i = 2
    while n % i != 0:
        i += 1
    print(i)  
n = int(input('Введите число (не меньше 2): '))
find_negative_pairs(n)
