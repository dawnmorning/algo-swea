import sys
sys.stdin = open('6190.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    danjo = list(map(int, input().split()))
    result = -1
    for i in range(n):
        for j in range(i+1, n):
            danjo_sep = str(danjo[i] * danjo[j])
            for k in range(0, len(danjo_sep)-1):
                if danjo_sep[k] > danjo_sep[k+1]:
                    break
            else:
                if result < int(danjo_sep):
                    result = int(danjo_sep)
    print(f'#{tc} {result}')

            # for k in range(0, len(danjo_li)-1):
            #     if danjo_li[k] > danjo_li[k+1]:
            #         break