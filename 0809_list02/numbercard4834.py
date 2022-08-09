import sys
sys.stdin = open('numcard.txt.txt')
T = int(input())
for case in range(1, T+1):
    n = int(input())
    value = int(input())
    room = [0] * 10
    for i in range(n):
        room[value % 10] += 1
        value = value // 10
    room_num = 0
    max_room = 0
    for j in range(len(room)):
        if room[j] >= max_room:
            max_room = room[j]
            room_num = j

    print(f'# {case} {room_num} {max_room}')


