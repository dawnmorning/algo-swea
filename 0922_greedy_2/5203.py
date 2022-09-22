import sys
sys.stdin = open('5203.txt')


t = int(input())
for tc in range(1, t+1):
    deck = list(map(int, input().split()))  # 카드 순서 12개
    p1 = [0] * len(deck)        # p1 카드 번호
    p2 = [0] * len(deck)        # p2 카드 번호 0 ~ 9
    value = 0
    for i in range(len(deck) // 2):
        p1[deck.pop(0)] += 1
        for j in range(10):
            if p1[j] >= 3 or (p1[j] and p1[j + 1] and p1[j + 2]):
                value = 1
        if value:
            break

        p2[deck.pop(0)] += 1
        for j in range(10):
            if p2[j] >= 3 or ( p2[j] and p2[j+1] and p2[j+2] ):
                value = 2
        if value:
            break
    print(f'#{tc} {value}')
