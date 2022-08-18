import sys
sys.stdin = open('4869.txt')
t = int(input())
def jaguar(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    else:
        return jaguar(n-1) + 2 * jaguar(n - 2)

for tc in range(1, t+1):
    width = int(input())
    width_num = width // 10
    cnt = jaguar(width_num)
    print(f'#{tc} {cnt}')
