import sys
sys.stdin = open('1213.txt', encoding = 'UTF-8')
t = 10
for tc in range(1,t+1):
    garbage = int(input())
    pattern = input()
    text = input()
    n = len(text)
    m = len(pattern)
    cnt = 0
    for i in range(n-m+1):
        if text[i] == pattern[0]:
            if text[i:i+m] == pattern:
                cnt+=1
    print(f'#{tc} {cnt}')

