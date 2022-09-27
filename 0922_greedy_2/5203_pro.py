import sys
sys.stdin = open('5203.txt')

def check_run(card):
    for i in range(8):  # 8,9 는 연속된 숫자가 3개가 안 되기 때문에 0~7까지만 순회
        if card[i] >= 1 and card[i+1] >=1 and card[i+2] >= 1:
            return True
    # not run
    return False


def baby_gin(cards):
    # 0 ~ 9 의 인덱스를 가지는 리스트를 생성
    # 각 인덱스는 카드 번호를 의미하고 값은 카드의 장수를 의미
    player1 = [0 for _ in range(10)]
    player2 = [0 for _ in range(10)]

    # 주어진 카드는 총 12장
    for idx in range(12):
        card_num = cards[idx] # idx 번째 뽑는 카드의 번호
        if idx % 2 == 0: # player1이 카드를 가져가는 순서
            player1[card_num] += 1 # 뽑은 카드를 카운팅
            if player1[card_num] == 3: # tri
                return 1
            if check_run(player1):      # run
                return 1
        else:           # plyaer2가 카드를 가져가는 순서
            player2[card_num] += 1  # 뽑은 카드를 카운팅
            if player2[card_num] == 3:  # tri
                return 2
            if check_run(player2):  # run
                return 2
    return 0


t = int(input())
for tc in range(1,t+1):
    cards = list(map(int, input().split())) # 카드 정보 받아오기 12장
    res = baby_gin(cards)
    print(f'#{tc} {res}')
