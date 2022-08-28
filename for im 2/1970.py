import sys
sys.stdin = open('1970.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    money = [50000,10000,5000,1000,500,100,50,10]
    arr = [0] * len(money)
    for i in range(len(money)):
        arr[i] = n // money[i]
        n = n % money[i]
    print(f'#{tc}')
    for j in arr:
        print(j, end = ' ')
    print()
