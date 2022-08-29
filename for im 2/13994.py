import sys
sys.stdin = open('13994.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    stop = [0] * 1001  # 1~1000번 정류장
    for _ in range(n):
        bus, a,b  = map(int, input().split())
        stop[a] += 1
        stop[b] += 1
        if bus == 1 : #일반
             for i in range(a+1, b):
                 stop[i] += 1
        elif bus == 2: # 급행, A가 짝수면
            # if a % 2== 0:
            #     for i in range(a+1, b):
            #         if i % 2 == 0:
            #             stop[i] += 1
            # else:
            #     for i in range(a+1, b):
            #         if i % 2 == 0:
            #             stop[i] += 1
            for i in range(a+2, b, 2):
                stop[i] += 1
        else:    # 광역
            if a % 2 == 0:
                for i in range(a+1, b):
                    if i % 4 == 0:
                        stop[i] += 1
            else:
                for i in range(a+1, b):
                    if i % 3 == 0 and i % 10 != 0 :
                        stop[i] += 1
    # max( range( len(A) ), key = lambda x: A[x])
    # maxidx = 0
    # for i in range(1001):
    #     if stop[maxidx] < stop[i]:
    #         maxidx = i
    print(f'#{tc} {max(stop)}')
