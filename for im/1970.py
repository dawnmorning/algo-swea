import sys
sys.stdin = open('1970.txt')
t = int(input())
for tc in range(1, t+1):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    value = int(input())
    print(f'#{tc}')
    for i in range(len(money)):
        print(value // money[i], end=' ')
        value = value % money[i]
    print()