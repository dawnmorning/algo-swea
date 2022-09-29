import sys
sys.stdin = open('5248.txt')
def make(i):

    p[i] = i

def find_p(x):

    while x != p[x]:
        x = p[x]
    return x

def union(x,y):

    p[find_p(y)] = find_p(x)

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    adj_list = list(map(int, input().split()))
    p = [0]*(N+1)
    arr = [[] for _ in range(M)]
    for i in range(1,N+1):
        make(i)

    for i in range(M):
        a, b = adj_list[2*i], adj_list[2*i + 1]
        arr[i] = [a,b]

    for i in range(M):
        union(arr[i][0],arr[i][1])

    for i in range(1,N+1):
        p[i] = find_p(i)

    res = len(set(p)) - 1
    print(f'#{tc} {res}')