import sys
sys.stdin = open('5204.txt')

def divided(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = divided(arr[:mid])
    right = divided(arr[mid:])
    return merge_sort(left, right)

def merge_sort(left, right):
    global cnt

    if right[-1] < left[-1]:
        cnt += 1

    result = []
    l = r = 0
    while len(left) > l or len(right) > r:
        if len(left) > l and len(right) > r:
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        elif len(left) > l :
            result.append(left[l])
            l += 1
        elif len(right) > r :
            result.append(right[r])
            r += 1
    return result

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    res = divided(arr)
    print(f'#{tc} {res[n//2]} {cnt}')