import sys
sys.stdin = open('input1206.txt')
for i in range(1,11):
    num_apart = int(input())
    apart = list(map(int,input().split()))
    count = 0
    for j in range(2,num_apart-2):
        if apart[j] >= apart [j-1] and apart[j] >= apart[j-2] and apart[j] > apart[j+1] and apart[j] > apart[j+2]:
            max_height_4=0
            for k in apart[j-1], apart[j-2],apart[j+1],apart[j+2]:
                if max_height_4<k:
                    max_height_4 = k
            count += apart[j] - max_height_4
    print(f'#{i} {count}')


