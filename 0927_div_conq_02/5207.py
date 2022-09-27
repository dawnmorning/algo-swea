import sys
# sys.stdin = open('5207.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for number in B:
        low = 0
        high = n-1
        flag = None
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == number:
                cnt += 1
                break
            elif A[mid] > number and flag != 'l':
                high = mid - 1
                flag = 'l'
            elif A[mid] < number and flag != 'r' :
                low = mid + 1
                flag = 'r'
            else:
                break
    print(f'#{tc} {cnt}')
