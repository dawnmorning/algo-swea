def inorder(a):
    if a <= n:
        inorder(a*2)
        print(ch[a], end = '')
        inorder(a*2+1)


import sys
sys.stdin = open('1231.txt')
t = 10
for tc in range(1, t+1):
    n = int(input())
    ch = [0] * (n+1)
    for i in range(n):
        adjlist = list(input().split())
        ch[i+1] = adjlist[1]
    print(f'#{tc}', end = ' ')
    inorder(1)
    print()



# v = int(input())
# list = [0] * (v+1)
# for i in range(v):
#     pot = list(input().split())
#     list[i+1] = pot[1]
