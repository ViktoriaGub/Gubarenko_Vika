#Задание 1-1
print('Курс Основы программирования начался')

#Задание 1-2
a=16823*12302/3092
print(a)

#Задание 1-3
age=int(input("Введите ваш возраст"))
d=input("Введите ваше имя")
if age >= 16:
print ('Поздравляем вы поступили в ВГУИТ')
else:
t=16-age
print('Сначала нужно окончить школу!','Вам ещё учится ', t ,"лет")
if age >0 and age<75:
print("Вы соответствуете возрастным рамкам")
else:
print("Вы не соответствуете возрастным рамкам")
if d=="Иван":
print("Вы Иван")
else:
print("Вы не Иван")

#Задание 1-4
seconds=int(input("Введите количество секунд"))
a=seconds//60
b=seconds//3600
c=seconds//86400
print("Секунд пройшло", seconds,"или прошло", a,"минут. Или пройшло", b,"часов. Или
пройшло ",c,"дней")

#Задание 1-5
n= int(input("Введите число"))
q=n+n**2+n**3+n**4+n**5
print("Ваш результат ",q)

#Задание 1-6
x=int(input("Ввести значение"))
y=int(input("Ввести значение"))
x,y=y,x
print("При обмене значения х=",x,"а у=",y)

#Задание 1-7
h=int(input("Ввести число"))
if h%2==0:
print("Ваше число чётное")
else:
print("Ваше число не чётное")