import sys
sys.stdin = open('13300.txt')
n,k = map(int,input().split())
male = [0] * 7
female = [0] * 7
for i in range(n):
    s, y = map(int, input().split())
    if s == 0:
        female[y] += 1
    else:
        male[y] += 1

room = 0
for j in range(1,7):
    if male[j] % k == 0:
        room = room + (male[j] // k)
    else:
        room = room + (male[j] // k) + 1
    if female[j] % k == 0 :
        room = room + (female[j] // k)
    else:
        room = room + (female[j] // k) + 1
print(room)
