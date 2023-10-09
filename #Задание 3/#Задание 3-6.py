def chess_board():
    n1 = int(input("Введите номер столбца"))
    n2 = int(input("Введите номер строки"))
    m1 = int(input("Введите номер столбца 2"))
    m2 = int(input("Введите номер строки 2"))
    d1 = 0
    d2 = 0
    if n1 or n2 %2==0:
        d1 = 1
    else:
        d1 = 0
    if m1 or m2 %2==0:
        d2 = 1
    else:
        d2 = 0
    if d1 == d2:
        print('Да')
    else:
        print('Нет')
chess_board()