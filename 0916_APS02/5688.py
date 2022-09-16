import sys
sys.stdin = open('5688.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    x = round(n ** (1/3))
    if x ** 3 == n:
        print(f'#{tc} {int(x)}')
    else:
        print(f'#{tc} {-1}')