def vid(n):
    if n < 10:
        print(n)
    else:
        vid(n // 10)
        print(n % 10)
n = int(input("Введите натуральное число: "))

print("Цифры числа N:")  
vid(n)