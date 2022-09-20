import sys
sys.stdin = open('1242.txt', 'r')
def cal(x,y,z):
    min_num = min(x,y,z)
    x //= min_num
    y //= min_num
    z //= min_num
    return str(x)+str(y)+str(z)
t = int(input())
hex = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A' :'1010',
    'B' :'1011',
    'C' :'1100',
    'D' :'1101',
    'E' :'1110',
    'F' :'1111',
}
pattern = {
    '211' : 0, '221' : 1, '122': 2, '411' : 3,
    '132' : 4, '231' : 5, '114': 6, '312': 7,
    '213' : 8, '112' : 9
}
for tc in range(1, t+1):
    n, m = map(int,input().split())
    code = [input() for _ in range(n)]
    ejin_li = [''] * n
    for i in range(n):
        for j in range(m):
            ejin_li[i] += hex[code[i][j]]
    visited, pw, total = [], [], 0
    for row in range(n):
        a,b,c = 0,0,0
        for col in range(m*4-1, -1, -1):
            if b == 0 and c == 0 and ejin_li[row][col] == '1':
                a += 1
            elif a > 0 and c == 0 and ejin_li[row][col] == '0':
                b += 1
            elif a > 0 and b > 0 and ejin_li[row][col] == '1':
                c += 1
            if a > 0 and b > 0 and c > 0 and ejin_li[row][col] == '0':
                pw.append(pattern[cal(c,b,a)])
                a,b,c= 0,0,0
            if len(pw) == 8:
                pw = pw[::-1]
                value = (sum(pw) + 2 * sum(pw[0:7:2]))

                if value % 10 == 0 and pw not in visited:
                    total += sum(pw)
                visited.append(pw)
                codes = []
    print(f'#{tc} {total}')


    


