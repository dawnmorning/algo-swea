import sys
sys.stdin = open('4615.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    othello = [[0] * n for _ in range(n)]
