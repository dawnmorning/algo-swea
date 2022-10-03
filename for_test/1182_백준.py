n, s = map(int, input().split())
temp = list(map(int, input().split()))
subset = [[]]

cnt= 0
for i in temp:
    length = len(subset)
    for j in range(length):
        subset.append(subset[j] + [i])

print(set(subset))
for num in subset:
    for n in num:
        if n > 0 and sum(num) == s:
            cnt += 1
print(cnt)

