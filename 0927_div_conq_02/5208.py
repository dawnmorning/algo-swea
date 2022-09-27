import sys
sys.stdin = open('5208.txt')
# def dfs(num):
#     global compare, cnt
#
#     if num >= busstop:
#         if cnt > compare:
#             cnt = compare
#         return
#     elif compare > cnt:
#         return
#
#     start = num
#     value = arr[start]
#     for i in range(start + value, 0 ,-1):
#         compare +=1
#         dfs(i)
#         compare -= 1
#
t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    busstop = arr[0]
    battery = [0] + arr[1:]
    max_list = [0 for i in range(busstop)]
    for i in range(busstop):
        max_list[i] = i + battery[i]

    change = -1
    objet = busstop
    j = 1
    while objet > 1:
        if max_list[j] >= objet:
            change += 1
            objet = j
            j = 1
        else:
            j += 1
    print(f'#{tc} {change}')
#     arr = list(map(int, input().split()))
#     busstop = arr[0]
#     compare = 0
#     cnt = 100 ** 2
#     dfs(1)
#     print(f'#{tc} {cnt - 1}')

