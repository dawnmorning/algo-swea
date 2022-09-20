import sys
sys.stdin = open('1240')

def scanner(arr):
    pwd = []
    for r in range(n):
        # 뒤에서 부터 스캔. (암호문이 전부 1로 끝나기 때문)
        for c in range(m-1, -1, -1):
            # 1이 나올때까지 체크
            if arr[r][c] == '0':
                continue
            # 1이 나온 다면 해당 자리부터 56개의 숫자를 가지고 암호문을 뽑아내기
            for pos in range(c - 56 + 1, c, 7):
                num_bit = arr[r][pos:pos+7]  # 암호 숫자비트
                pwd.append(patterns[num_bit])  # 암호 숫자

            odd_num = pwd[0] + pwd[2] + pwd[4] + pwd[6]
            even_num = pwd[1] + pwd[3] + pwd[5] + pwd[7]

            if (odd_num * 3 + even_num) % 10 == 0:
                return odd_num + even_num
            else:
                return 0


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split()) # N : 가로 , m ; 세로
    arr = [input() for _ in range(n)] # 암호문이 포함된 data

    patterns = {
        '0001101' : 0,
        '0011001' : 1,
        '0010011' : 2,
        '0111101' : 3,
        '0100011' : 4,
        '0110001' : 5,
        '0101111' : 6,
        '0111011' : 7,
        '0110111' : 8,
        '0001011' : 9,

    }
    res = scanner(arr)
    print(f'#{tc} {res}')