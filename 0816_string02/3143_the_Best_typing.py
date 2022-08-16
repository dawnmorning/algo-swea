import sys
sys.stdin = open('3143.txt')
t = int(input())
for tc in range(1, t+1):
    a, b = map(str, input().split())
    cnt = 0
    t = len(a)
    p = len(b)
    i = 0
    while i < t:
        if a[i] == b[0]:
            if b[:p] == a[i:i+p]:
                cnt += 1
                i = i+p
            else:
                cnt += 1
                i = i+1
        else:
            cnt += 1
            i = i + 1
    print(f'#{tc} {cnt}')

    #while 과 for의 차이를 잘 알자, for는 i + p 해도 for i 에서 초기화 된다.