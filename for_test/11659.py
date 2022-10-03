import sys
input = sys.stdin.readline
n , m = map(int, input().split())
numbers = list(map(int, input().split()))
for _ in range(m):
    a, b= map(int, input().split())
    value = 0
    for i in range(a-1, b):
        value += numbers[i]
    print(value)