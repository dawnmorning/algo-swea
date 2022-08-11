import sys
sys.stdin = open('4837.txt')
a = int(input())
for tc in range(1, a+1):
    n, k = map(int,input().split())
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    value = len(A)
    cnt = 0
    for i in range(1<<value):
        li = []
        total = 0
        for j in range(value):
            if i & (1<<j):
                li.append(A[j])  #부분집합 전체 추가하기
                total += A[j]   #부분집합 별로 합을 만든다.  for i에 total = 0 을 추가해 뒀으므로 해당 부분집합 계산 후 초기화
        if len(li) == n and total == k:
            cnt += 1
        print(li)
    print(f'#{tc} {cnt}')







