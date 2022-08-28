import sys
sys.stdin = open('2072.txt')
t = int(input())
for tc in range(1, t + 1):
    number = list(map(int, input().split()))
    number_odd=[]
    for i in number:
        if i% 2 == 1:
            number_odd.append(i)
    print(f'#{tc} {sum(number_odd)}')