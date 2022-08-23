import sys
sys.stdin = open('4875.txt')
t = int(input())
def mazerunner(maze,n):
    start = [0,0]
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start[0], start[1] = i, j
                break

    #start = [4,3]에서 시작
    moving_r = [-1, 1, 0 ,0]
    moving_c = [0, 0, -1 ,1]
    sizak = start
    stack = []
    while True:
        for j in range(4):
            dr = sizak[0] + moving_r[j]
            dc = sizak[1] + moving_c[j]
            if 0 <= dr < n and 0 <= dc < n:
                if maze[dr][dc] == 0:
                    stack.append(sizak)
                    sizak = [dr, dc]
                    maze[dr][dc] = 1
                    break
                if maze[dr][dc] == 3:
                    return 1
                    break
        else:
            if stack:
                sizak = [stack[-1][0], stack[-1][1]]
                stack.pop()
            else:
                return 0
for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    value = mazerunner(maze,n)
    print(f'#{tc} {value}')

# import sys
# sys.stdin = open('4875.txt')
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     maze = [list(map(int, input())) for _ in range(n)]
#     start = [0, 0]
#     for i in range(n):
#         for j in range(n):
#             if maze[i][j] == 2:
#                 start[0], start[1] = i, j
#                 break
#
#     # start = [4,3]에서 시작
#     moving_r = [-1, 1, 0, 0]
#     moving_c = [0, 0, -1, 1]
#     sizak = start
#     stack = []
#     while stack:
#         for j in range(4):
#             dr = sizak[0] + moving_r[j]
#             dc = sizak[1] + moving_c[j]
#             if 0 <= dr < n and 0 <= dc < n:
#                 if maze[dr][dc] == 0:
#                     stack.append(sizak)
#                     sizak = [dr, dc]
#                     maze[dr][dc] = 1
#                     break
#                 if maze[dr][dc] == 3:
#                     print(f'#{tc} 1')
#                     break
#         else:
#             if stack:
#                 sizak = [stack[-1][0], stack[-1][1]]
#                 stack.pop()
#             else:
#                 print(f'#{tc} 0')



