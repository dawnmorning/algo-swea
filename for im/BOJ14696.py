import sys
sys.stdin = open('14696.txt')

n = int(input())
for _ in range(n):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    li_a = a.pop(0)
    lib_b = b.pop(0)
    cntA = [0] * 4
    cntB = [0] * 4
    for i in range(4, 0 ,-1):
        for j in a :
            if i == j:
                cntA[4 - j] += 1
        for j in b :
            if i == j:
                cntB[4 - j] += 1
    for i in range(4):
        if cntA[i] > cntB[i]:
            print('A')
            break
        if cntB[i] > cntA[i]:
            print('B')
            break
    else:
        print('D')

