import sys
sys.stdin = open('1240')
t = int(input())
for tc in range(1, t+1):
    n,m = map(int, input().split())
    ref = {
        '0001101' : 0,
        '0011001': 1,
        '0010011' : 2,
        '0111101' : 3,
        '0100011' : 4,
        '0110001' : 5,
        '0101111' : 6,
        '0111011' : 7,
        '0110111' : 8,
        '0001011' : 9
    }
    bits = []
    for _ in range(n):
        bit = input()
        idx = 0
        if bits:
            continue
        while idx < m - 7:
            idx += 1
            if bit[idx : idx+7] in ref and not int(bit[idx+7]):
                bits.append(ref[bit[idx: idx+7]])
                idx += 6
    sumV = sum(bits) if not (sum(bits) + 2 * sum(bits[0:7:2])) % 10 else 0
    print(f'#{tc} {sumV}')
