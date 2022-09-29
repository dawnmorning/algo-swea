import sys
sys.stdin = open('5247.txt')

def BFS(n,m):
    front = rear = -1  # queue의 시작을 위해 초기화
    calculated[n] = 1

    # queue의 입력
    rear += 1
    q[rear] = n

    while front != rear:  # queue가 비어있는지 확인
        # queue에서 꺼내기 (선형 큐는 따로 삭제하지는 않을 것임)
        front += 1
        num = q[front]
        operator = [num + 1, num - 1, num * 2 , num - 10] # 4개의 계산된 결과가 나오게 됨

        for i in range(4):
            if operator[i] == m: # 만드려는 m이 완성되었다면
                return calculated[num]

        if 0 < operator[i] <= 1000000:
            if calculated[operator[i]] == 0:            # 아직 계산되지 않은 값이라면
                calculated[operator[i]] = calculated[num] + 1
                # queue에 계산해야할 숫자를 추가
                rear += 1
                q[rear] = operator[i]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())

    q = [0] * 1000001
    calculated = [0] * 1000001  # 몇 번 계산했는지 카운트를 이곳에 저장

    res = BFS(n, m)
    print(f'#{tc} {res}')