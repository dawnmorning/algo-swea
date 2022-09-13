def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    for i in arr1:
        map = []
        for _ in range(n):
            num = i % 2
            i = i // 2
            map.insert(0,num)
        map1.append(map)
    for j in arr2:
        map = []
        for _ in range(n):
            num = j % 2
            j = j // 2
            map.insert(0,num)
        map2.append(map)
    for k in range(n):
        map = ''
        for l in range(n):
            if map1[k][l] == 1 or map2[k][l] == 1:
                map += '#'
            else:
                map += ' '
        answer.append(map)
    return answer