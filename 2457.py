import sys
sys.stdin = open('2457.txt')
input = sys.stdin.readline
n = int(input())
date = []
for _ in range(n):
    temp = list(map(int, input().split()))
    date.append([temp[0] * 100 + temp[1], temp[2] * 100 + temp[3]])
date.sort(key= lambda x : (x[0], x[1]))
cnt = 0
start_date = 301
end = 0
while date:
    if start_date >= 1201 or start_date < date[0][0]:
        break
    for i in range(len(date)):
        if start_date >= date[0][0]:
            if end <= date[0][1]:
                end = date[0][1]
            date.remove(date[0])
        else:
            break
    start_date = end
    cnt += 1
if start_date < 1201:
    print(0)
else:
    print(cnt)
