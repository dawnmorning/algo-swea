#사다리 #1210
# import sys
# sys.stdin = open('1210.txt')
# for _ in range(10):
#     tc = input()
#     ladder = [list(map(int, input().split()))for _ in range(100)]
#     for j in range(100):
#         if ladder[99][j] == 2:
#             col = j
#     dr = [-1,0,0]
#     dc = [0,1,-1]
#     row = 99
#     while row != 0:
#         for k in range(3):
#             now_row = row + dr[k]
#             now_col = col + dc[k]
#             if 0 <= now_row < 100 and 0 <= now_col < 100:
#                 if ladder[now_row][now_col] == 1:
#                     ladder[row][col] = 0
#                     row = now_row
#                     col = now_col
#     print(f'#{tc} {col}')

# 이진 탐색 4839
# import sys
# sys.stdin = open('4839.txt')
# t = int(input())
# for tc in range(1, t+1):
#     P, pa, pb = map(int,input().split())
#
#     left = 1
#     right = P
#     cntA = mid = cntB = 0
#     while mid != pa:
#         mid = int((left + right) // 2)
#         if mid == pa:
#             break
#         elif mid < pa:
#             left = mid
#         else:
#             right = mid
#         cntA += 1
#
#     left = 1
#     right = P
#     mid = 0
#     while mid != pb:
#         mid = int((left + right) // 2)
#         if mid == pb:
#             break
#         elif mid > pb:
#             right = mid
#         else:
#             left = mid
#         cntB += 1
#     if cntA > cntB:
#         result = 'B'
#     if cntA < cntB:
#         result = 'A'
#     else:
#         result = 0
#     print(f'#{tc} {result}')

# 특별한 정렬 4843

# import sys
# sys.stdin = open('4843.txt')
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     last= []
#     for i in range(n-1,-1,-1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     for k in range(5):
#         last.append(arr[n - k -1])
#         last.append(arr[k])
#     print(f'#{tc}', end= ' ' )
#     for l in range(10):
#         print(f'{last[l]}', end = ' ')
#     print()

# 색칠하기 learn list2
# import sys
# sys.stdin = open('4836.txt')
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     arr = [[0] * 10 for _ in range(10)]
#     for i in range(n):
#         r1,c1,r2,c2,color = map(int,input().split())
#         for j in range(r1, r2+1):
#             for k in range(c1, c2+1):
#                 arr[j][k] += color
#     cnt = 0
#     for l in range(10):
#         for m in range(10):
#             if arr[l][m] == 3:
#                 cnt += 1
#     print(f'#{tc} {cnt}')

# 2001파리퇴치
# import sys
# sys.stdin = open('2001.txt')
# t = int(input())
# for tc in range(1, t+1):
#     n, m = map(int,input().split())
#     fly = [list(map(int, input().split()))for _ in range(n)]
#     max_fly = 0
#     for i in range(n-m+1):
#
#         for j in range(n-m+1):
#             pre_max = 0
#             for k in range(m):
#                 for l in range(m):
#                     pre_max += fly[k+i][l+j]
#                     if pre_max > max_fly:
#                         max_fly = pre_max
#     print(f'#{tc} {max_fly}')

# 1979 어디에 단어가 들어갈 수 있을까

# import sys
# sys.stdin = open('1979.txt')
# t = int(input())
# for tc in range(1, t+1):
#     n , m = map(int, input().split())
#     puz = [list(map(int, input().split()))for _ in range(n)]
#     result = 0
#     for i in range(n):
#         cnt = 0
#         for j in range(n):
#             if puz[i][j] == 1:
#                 cnt += 1
#             if puz[i][j] == 0 or j == n-1:
#                 if cnt == m:
#                     result += 1
#                 if puz[i][j] == 0:
#                     cnt = 0
#     for i in range(n):
#         cnt = 0
#         for j in range(n):
#             if puz[j][i] == 1:
#                 cnt += 1
#             if puz[j][i] == 0 or j == n - 1:
#                 if cnt == m:
#                     result += 1
#                 if puz[j][i] == 0:
#                     cnt = 0
#     print(f'#{tc} {result}')

# 1974 스도쿠 검증
import sys
sys.stdin = open('1974.txt')
t = int(input())
for tc in range(1, t+1):
    sdoku = [list(map(int, input().split()))for _ in range(9)]
    cnt = 0
    for i in range(9):
        multiple_R = 1
        multiple_C = 1
        for j in range(9):
            multiple_R = sdoku[i][j] * multiple_R
            multiple_C = sdoku[j][i] * multiple_C
            if multiple_R == multiple_C == 1*2*3*4*5*6*7*8*9 :
                cnt += 1
                break
    for i in range(0,7,3):
        for j in range(0,7,3):
            multiple_rec = 1
            for k in range(3):
                for l in range(3):
                    multiple_rec = sdoku[k+i][l+j] * multiple_rec
                    if multiple_rec == 1*2*3*4*5*6*7*8*9 :
                        cnt+=1
                        break
    if cnt == 18:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')





