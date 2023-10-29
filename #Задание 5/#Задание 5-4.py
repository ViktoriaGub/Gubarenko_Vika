x = float(input('Введите сколько км пробежал споресмен в 1 день  '))
y = float(input('Введите  y километров  '))
a = 1
di = x
while di < y:
    di += di * 0.1
    a += 1
print(a)
