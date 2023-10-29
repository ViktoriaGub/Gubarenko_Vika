def print_negative_pairs():
    a = []
    for i in range(10):
        n = int(input(f"Введите число {i+1}: "))
        a.append(n)
    for i in range(len(a) - 1):
        if a[i] < 0 and a[i+1] < 0:
            print(a[i], a[i+1])

print_negative_pairs()