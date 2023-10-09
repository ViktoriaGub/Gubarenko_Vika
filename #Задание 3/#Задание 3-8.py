def matching():
    a = int(input("введите число"))
    b = int(input("введите число"))
    c = int(input("Введите число"))
    if a == b == c:
        print(3)
    elif a == b or b == c or a == c:
        print(2)
    else:
        print(0)
matching()       