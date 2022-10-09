import sys
sys.stdin = open('4340.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    info = [list(map(int, input().split()))for _ in range(n)]
