import sys
sys.stdin = open('5176.txt')
def inorder(a):
    global num
    if a <= n:
        inorder(2*a)
        tree[a] = num
        num += 1
        inorder(2*a + 1)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    tree = [0] * (n+1)
    num = 1
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[n//2]}')
