import sys
sys.stdin = open('4864.txt')
t = int(input())
for tc in range(1,t+1):
    str_1 = input()
    str_2 = input()
    cnt = 0
    for i in range(len(str_2)):
        if str_1[:] == str_2[i:i+len(str_1)]:
            cnt = 1
    print(f'#{tc} {cnt}')

t = int(input())
for tc in range(1, t+1):
    n = input()
    m = input()
    print(f'#{tc} {int(n in m)}')