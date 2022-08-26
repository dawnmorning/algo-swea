import sys
sys.stdin = open('1966.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    number = list(map(int,input().split()))
    number = sorted(number)
    print(f'#{tc}', end= ' ')
    for i in number:
        print(i, end = ' ')
    print()
