import sys
sys.stdin = open('input_num2.txt')
n = int(input())
for i in range(n):
    value = int(input())
    room = [0] * 12
    for j in range(6):
        room[value % 10] += 1
        value = value // 10
    finding = tri = run = 0
    while finding < 10:
        if room[finding] >= 3:
            tri += 1
            room[finding] -= 3
            continue

        if room[finding] >=1 and room[finding+1] >=1 and room[finding+2] >=1:
            run += 1
            room[finding] -= 1
            room[finding+1] -= 1
            room[finding+2] -= 1
            continue
        finding += 1

    if tri + run == 2:
        print(f'#{i + 1} 1')
    else:
        print(f'#{i + 1} 0')
