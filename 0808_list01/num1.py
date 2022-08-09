import sys
sys.stdin = open('input_num1.txt')
for case in range(1, int(input())+1):
    n = int(input())
    li = list(map(int, input().split()))
    max_value = 0

    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            if li[i] > li[j]:
                cnt += 1

        if cnt > max_value:
            max_value = cnt

    print(f'#{case} {max_value}')