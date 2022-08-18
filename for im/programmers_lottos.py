def solution(lottos, win_nums):
    cnt = lottos.count(0)
    rank = [6,6,5,4,3,2,1]
    value = 0
    for i in win_nums:
        if i in lottos:
            value += 1
    return rank[value+cnt], rank[value]