import sys
sys.stdin = open('4012.txt')

def comb(ingredient):
    value = 0
    for i in range(n//2):
        for j in range(n//2):
            value += food[ingredient[i]][ingredient[j]] + food[ingredient[j]][ingredient[i]]
        return value

def dfs(a,b):
    global minV
    if a == n //2:
        one = []
        two = []
        for i in range(n):
            if visited[i]:
                one.append(i)
            else:
                two.append(i)
        food1 = comb(one)
        food2 = comb(two)
        if abs(food1 - food2) < minV:
            minV = abs(food1 - food2)
        return
    for i in range(b,n):
        if not visited[i]:
            visited[i] = 1
            dfs(a+1,i+1)
            visited[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    food = [list(map(int, input().split())) for _ in range(n)]
    minV = 1000000
    visited = [0] * n
    dfs(0,0)
    print(f'#{tc} {minV}')
