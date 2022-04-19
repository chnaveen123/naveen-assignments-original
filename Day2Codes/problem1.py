n = int(input())
matrix = [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
print("matrix of {} * {} :".format(n, n))
for m in matrix:
    print(m)
