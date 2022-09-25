import sys
sys.stdin = open('5174.txt')

def preorder(n):
    global cnt
    if n :
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])
    return cnt
t = int(input())
for tc in range(1,t+1):
    e, n = map(int, input().split())
    tree = list(map(int, input().split()))
    ch1 = [0] * (e+2)
    ch2 = [0] * (e+2)
    for i in range(e):
        p, c = tree[2*i], tree[2*i + 1]
        if ch1[i] == 0:
            ch1[i] = c
        else:
            ch2[i] = c
    cnt = 0
    print(f'#{tc} {preorder(n)}')