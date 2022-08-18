# import sys
# sys.stdin = open('prac2.txt')
# t = int(input())
#
# for tc in range(1,t + 1):
#     vps = list(input())
#     total = 0
#
#     for i in vps:
#         if i == "(":
#             total +=1
#         elif i == ")":
#             total -=1
#     print(f'#{tc}', end=' ')
#     if total == 0:
#         print("1")
#     elif total>0:
#         print("-1")
#     elif total < 0 :
#         print("-1")
import sys
sys.stdin = open('prac2.txt')
t = int(input())
for tc in range(1, t+1):
    value = input()
    li = []
    for i in value:
        if i == '(':
            li.append(i)
        elif i == ')':
            if li:  # li안에 ( 있으면
                li.pop()     #(날리기
            else:
                cnt = -1
                break
    else:
        if li:
            cnt = -1
        else:
            cnt = 1

    print(f'#{tc} {cnt}')
