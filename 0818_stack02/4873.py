import sys
sys.stdin = open('4873.txt')
t = int(input())
for tc in range(1, t+1):
    value = list(map(str,input()))
    i = 0
    while i+1 < len(value):
        if value[i] == value[i+1]:
            value.pop(i+1)
            value.pop(i)
            i -= 1
        else:
            i += 1
    print(f'#{tc} {len(value)}')
