import sys
sys.stdin = open('4408.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    room = [0] * 200
    for _ in range(n):
        now, back = map(int,input().split())
        if now > back:
            now, back = back, now
        for i in range((now-1)//2 , (back-1)//2+1):
            room[i] += 1
    print(f'#{tc} {max(room)}')


