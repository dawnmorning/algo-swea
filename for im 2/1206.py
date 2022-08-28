import sys
sys.stdin = open('1206.txt')
t = 10
for tc in range(1, t+1):
    n = int(input())
    apart = list(map(int, input().split()))
    result = 0
    for i in range(2, n-2):
        if apart[i] > apart[i-1] and apart[i] > apart[i-2] and apart[i] > apart[i+1] and apart[i] > apart[i+2]:
            possible_view = apart[i]
            value = 0
            for j in apart[i-1],apart[i-2],apart[i+1],apart[i+2]:
                if value < j:
                    value = j
            result += possible_view - value
    print(f'#{tc} {result}')