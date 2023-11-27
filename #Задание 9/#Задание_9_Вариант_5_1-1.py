def sormatrix(matrix):
    somatrix = []
    for row in matrix:
        srow = sorted(row)
        somatrix.append(srow)
    return somatrix
matrix=[[4, 5, 7, 3, 10, 21]]

somatrix = sormatrix(matrix)
print(somatrix)