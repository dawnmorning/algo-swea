# import sys
# sys.stdin = open('4836.txt')
T = int(input())
for tc in range(1,T+1):
    number = int(input())
    arr = [[0] * 10 for _ in range(10)] #0으로 10 * 10 판 만들기
    cnt = 0   #전체 값은 항상 젤 위에
    for _ in range(1, number+1):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1,r2+1):   #행으로 r1에서 r2+1까지
            for j in range(c1,c2+1): #열로 c1에서 c1+1까지 1로 채운다!!!!
                arr[i][j] += 1
                if arr[i][j] == 2:  #근데 케이스들에서 겹치는 부분은 2가 될것이므로
                    cnt += 1    #퍼플색이 된다.
    print(f'#{tc} {cnt}')



