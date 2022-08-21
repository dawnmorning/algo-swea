#인접한 두 원소를 비교하여 자리를 계속 교환하는 방식
#첫번째 원소부터 인접한 원소끼리 계속 자리를 교환하며 맨 마지막까지 이동한다.
def bubble(a, N):
    for i in range(n-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
