def find_second_largest(numbers):
    if len(numbers) == 0:
        return None

    max_num = max(numbers)
    numbers.remove(max_num)

    # Находим максимальный элемент в обновленном списке
    second_max = max(numbers)
    return second_max

numbers = []
while True:
    num = int(input("Введите число (0 для окончания ввода): "))
    if num == 0:
        break
    numbers.append(num)

second_largest = find_second_largest(numbers)
print("Второй по величине элемент:", second_largest)

input("Нажмите Enter для выхода")
