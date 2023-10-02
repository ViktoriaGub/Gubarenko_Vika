
seconds = int(input("Введите количество секунд: "))
a = seconds // 86400
h = (seconds % 86400) // 3600
m = (seconds % 3600) // 60
s = seconds % 60

print("Прошло", a, "дней,", h, "часов,", m, "минут,", s, "секунд.")