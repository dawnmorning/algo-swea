# import sys
# sys.stdin = open('1216.txt')
# t = 10
# for tc in range(1, t+1):
#     a = input()
#     arr = [list(map(str, input()))for _ in range(100)]
#     length = 0
#     for i in range(100):
#         for j in range(100):
#             if arr[i][i:i+j+1] == arr[i][i:i+j+1][::-1]:
#                 if len(arr[i][i:i+j+1]) > length:
#                     length = len(arr[i][i:i + j + 1])
#     print(length)
'''  9
    9
    11
    11
    14
    9
    9
    9
    10
    12'''
import sys
sys.stdin = open('1216.txt')
t = int(input())
for tc in range(1,1+t):
    t = int(input())
    arr = [list(input()) for _ in range(100)]
    rev_arr = list(zip(*arr))


    ans = []
    for k in range(100,0,-1):
        for i in range(100):
            for j in range(100-k+1):
                if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                    if len(ans) == 0:
                        ans.append(k)
                    else:
                        if ans[-1] < k:
                            ans.append(k)

    for k in range(100,0,-1):
        for i in range(100):
            for j in range(100 - k + 1):
                if rev_arr[i][j:j + k] == rev_arr[i][j:j + k][::-1]:
                    if len(ans) == 0:
                        ans.append(k)
                    else:
                        if ans[-1] < k:
                            ans.append(k)


    print(f'#{tc} {ans[-1]}')
