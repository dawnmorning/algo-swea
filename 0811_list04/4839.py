import sys
sys.stdin = open('4839.txt')
T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    left = 1
    right = P
    # A의 경우
    cntA = 0
    while left != right:
        middle = (left + right) // 2
        if middle == A:
            cntA += 1
            break
        if middle < A:
            left = middle
            cntA += 1
        else:
            right = middle
            cntA += 1
    # B의 경우
    left = 1
    right = P
    cntB = 0
    while left != right:
        middle = (left + right) // 2
        if middle == B:
            cntB += 1
            break
        if middle < B:
            right = middle
            cntB += 1
        else:
            left = middle
            cntB +=1

    if cntA > cntB:
        print(f'#{tc} B')
    if cntB > cntA:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')
