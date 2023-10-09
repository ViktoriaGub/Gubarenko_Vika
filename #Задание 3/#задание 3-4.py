def calculate_shoelace_length():
    a = int(input("Введите расстояние между рядами: "))
    b = int(input("Введите расстояние между дырочками в ряду: "))
    l = int(input("Введите длину свободного конца шнурка: "))
    N = int(input("Введите количество дырочек в каждом ряду: "))
    h = 2 * a * 2
    w = b * N
    f = l * 2
    t = h + w + f
    print("Искомая длина шнурка:", t)
calculate_shoelace_length()