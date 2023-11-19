def sormatrix(matrix):
    somatrix = []
    for row in matrix:
        srow = sorted(row)
        somatrix.append(srow)
    return somatrix

n = int(input('Введите размер: '))
matrix = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите элемент:')
        b.append(int(input()))
    matrix.append(b)

somatrix = sormatrix(matrix)
print(somatrix)
somatrix = sormatrix(matrix)
print(somatrix)