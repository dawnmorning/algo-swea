rectang = [[0] * 100 for _ in range(100)]
for _ in range(4):
    a,b,c,d = map(int,input().split())

    for i in range(a,c):
        for j in range(b,d):
            rectang[i][j] = 1

total = 0
for row in rectang:
    total += sum(row)
print(total)

