# import sys
# sys.stdin = open('1206.txt')
t = 10
for tc in range(1, t+1):
    num = int(input())
    building = list(map(int,input().split()))
    sum_building = 0
    for i in range(2,num-2):
        if building[i] > building[i-1] and building[i] > building[i-2] and building[i] > building[i+1] and building[i] > building[i+2]:
            test_building = 0
            for j in building[i-2], building[i-1], building[i+1], building[i+2]:
                if test_building < j:
                    test_building = j
            sum_building += building[i] - test_building
    print(f'#{tc} {sum_building}')
