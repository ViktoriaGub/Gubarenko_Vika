def find_negative_pairs(a):
    for i in range(len(a) - 1):
        if a[i] < 0 and a[i+1] < 0:
            print(a[i], a[i+1])

a = [-2, -3, 7, 0, -3, -5, 2, -8, -4, 6]
find_negative_pairs(a)