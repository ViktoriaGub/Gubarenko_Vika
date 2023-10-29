def remove_duplicates():
    a = []
    for i in range(10):
        n = int(input(f"Введите число {i+1}: "))
        a.append(n)
    b=list(set(a))
    print(b)
remove_duplicates()