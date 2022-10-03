n, m = map(int, input().split())
numbers = list(map(int, input().split()))
length = len(numbers)
maxV = 0
for i in range(length - 2):
    for j in range(i+1, length-1):
        for k in range(j+1, length):
            if (numbers[i] + numbers[j] + numbers[k] > m):
                continue
            else:
                maxV = max(maxV, numbers[i] + numbers[j] + numbers[k])
print(maxV)
