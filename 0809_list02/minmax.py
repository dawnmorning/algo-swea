import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for case in range(1, T+1):
    cnt = int(input())
    num = list(map(int,input().split()))
    max_num = num[0]
    min_num = num[0]
    for i in range(1, len(num)):
        if num[i] > max_num:   #[i+1]하고 비교하면  index out of range 기준점 하나를 잡고 업데이트 해나가야한다.
            max_num = num[i]
        if num[i] < min_num:
            min_num = num[i]
    print(f'#{case} {max_num - min_num}')


