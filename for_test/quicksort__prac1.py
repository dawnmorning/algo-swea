def quicksort(number):

    if len(number) <= 1:
        return number
    l = []
    r = []
    pivot = number[len(number)//2]
    for i in range(len(number)):
        if i == len(number)//2 :
            continue
        if pivot > number[i]:
            l.append(number[i])
        else:
            r.append(number[i])
    return quicksort(l) + [pivot] + quicksort(r)


t = int(input())
for tc in range(1, t+1):
    li = list(map(int, input().split()))
    res = quicksort(li)
    print(res)