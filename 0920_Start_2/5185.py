import sys
sys.stdin = open('5185.txt')
t = int(input())
ref = {
    'A' :10,
    'B' :11,
    'C' :12,
    'D' :13,
    'E' :14,
    'F' :15,
}
for tc in range(1, t+1):
    n, hexa = input().split()
    result = ''
    for r in hexa[::-1]:
        if r in ref:
            r = ref[r]
        r = int(r)
        for _ in range(4):
            result = str(r % 2) + result
            r = r//2
    print(f'#{tc} {result}')