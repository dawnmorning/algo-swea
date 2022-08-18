def memoization():
    n = 10
    for row in range(n):
        for col in range(row+1):
            if col == 0 or col == row:  #마지막은 row
                arr[row].append(1)
            else:
                arr[row].append(arr[row-1][col-1] + arr[row-1][col])
arr = [[]for _ in range(10)]
memoization()
t = int(input())
for tc in range(1, t+1):
    n = int(input())


    print(f'#{tc}')
    for row in range(10):
        for col in range(len(arr[row])):
            print(arr[row][col], end = ' ')
        print()

