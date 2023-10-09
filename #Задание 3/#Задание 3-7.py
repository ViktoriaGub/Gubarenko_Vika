def leap_year():
    y = int(input("Выведите 4-х значное число"))
    if (y % 4 == 0 and y%100 != 0) or (y%400 == 0): 
        print("Высокосный")
    else:
        print("Обычный")
leap_year()