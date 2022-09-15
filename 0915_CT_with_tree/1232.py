import sys
sys.stdin = open('1232.txt')

# def postorder(n):
#     global st
#     if n:
#         postorder(ch1[n])
#         postorder(ch2[n])
#         if st:
#             if tree[n] in sachicks:
#                 n2 = st.pop()
#                 n1 = st.pop()
#                 if tree[n] == '+':
#                     st.append(n1 + n2)
#                 elif tree[n] == '-':
#                     st.append(n1-n2)
#                 elif tree[n] == '*':
#                     st.append(n1*n2)
#                 elif tree[n] == '/':
#                     st.append(n1//n2)
#             else:
#                 st.append(tree[n])
#         else:
#             st.append(tree[n])

t = 10
for tc in range(1, t+1):
    n = int(input())
    m = n+1
    tree = [0] * m
    ch1 = [0] * m
    ch2 = [0] * m
    sachicks = ['+', '-', '*', '/']
    for _ in range(n):
        li = list(input().split())
        if len(li) == 4:
            p, sachick, l,r = int(li[0]), li[1], int(li[2]), int(li[3])
            tree[p] = sachick
            ch1[p] = l
            ch2[p] = r
        else:
            p, val = int(li[0]), int(li[1])
            tree[p] = val
    print(tree)
    # st = []
    # postorder(1)
    # print(f'#{tc} {int(st[-1])}')


