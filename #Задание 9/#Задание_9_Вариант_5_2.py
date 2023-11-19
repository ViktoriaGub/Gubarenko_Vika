def replace_elements(matrix):
    for row in matrix:
        min_element = min(row)
        for i, element in enumerate(row):
            if element == min_element:
                row[i] = 0 if element % 2 == 0 else 1
    return matrix

n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))

matrix = []
for i in range(n):
    row = list(map(int, input(f"Введите элементы {i+1}-й строки через пробел: ").split()))
    matrix.append(row)

new_matrix = replace_elements(matrix)
for row in new_matrix:
    print(row)