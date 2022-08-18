import sys
sys.stdin = open('2005.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[]for _ in range(n)]
    for row in range(n):
        for col in range(row+1):
            if col == 0 or col == row:  #마지막은 row
                arr[row].append(1)
            else:
                arr[row].append(arr[row-1][col-1] + arr[row-1][col])
    print(f'#{tc}')
    for row in range(n):
        for col in range(len(arr[row])):
            print(arr[row][col], end = ' ')
        print()

