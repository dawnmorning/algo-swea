# import sys
# sys.stdin = open('5186.txt')
# t = int(input())
# for tc in range(1, t+1):
#     n = float(input())
#     value = ''
#     i = 1
#     while i < 13:
#         n = n * 2
#         if n >= 1:
#             n -= 1
#             value += '1'
#         else:
#             value += '0'
#         if n == 0:
#             print(f'#{tc} {value}')
#             break
#         i+=1
#     else:
#         print(f'#{tc} overflow')
a = '111'
if len(a) == 3:
    a = '0' + a
print(a)