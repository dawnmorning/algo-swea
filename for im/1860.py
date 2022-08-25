import sys
sys.stdin = open('1860.txt')
t = int(input())
for tc in range(1, t+1):
    n,m,k = map(int,input().split())
    person = list(map(int, input().split()))
    person = sorted(person)
    for i in range(n): # 모든 손님에 대해
        total = (person[i] // m) * k # 도착까지 나온 빵의 갯수를 계산
        num = i + 1 # 나까지 손님 수
        if total < num :
            result = "Impossible"
            break
    else:  # 다 돌고 그래도 아닌 경우!
        result = 'Possible'

    print(f'#{tc} {result}')
