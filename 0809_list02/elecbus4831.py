import sys
sys.stdin = open('elecbus.txt')
t = int(input())
for case in range(t):
    can_go, last_stop, charger = map(int, input().split())
    charger_num = list(map(int, input().split()))
    bus = 0
    cnt = 0
    # for i in range(0,stop_num+1,can_go):
    #     for j in charger_num:
    #         if i == j:
    #             cnt += 1
    #         if i != j:  # 최대n 씩 움직일 수 있는데 최대 만큼이 아니라면 어떻게 할지이런 방식으로 대신 풀어 보실분..?
    while True:
        move_bus = 0
        if bus + can_go >= last_stop:
            break
        for i in charger_num:
            if bus < i <= bus + can_go:
                move_bus = i
        if move_bus == 0:
            cnt = 0
            break
        bus = move_bus
        cnt += 1
    print(f'#{case+1} {cnt}')





