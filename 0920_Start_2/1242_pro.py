import sys
sys.stdin = open('1242.txt')

def scanner(arr):
    total = 0
    for row in range(n):
        # 1자리의 16진수가 m개 있는데,
        # 이 16진수를 2진수 4자리로 변경했기 때문에 m * 4
        # index 탐색을 할 것이기에  -1 까지
        col = m * 4 -1
        while col >= 55: # 55번째의 리스트의 값이 1이 아니라면 앞에는 암호코드가 존재하지 않는 것이기 때문에 덜 봐도 됨
            if arr[row][col] == '1':  # 마지막 자리가 1일때,
                pwd = []
                for _ in range(8): # 8자리 숫자를 찾음
                    n1=n2=n3=n4 = 0

                    while arr[row][col] == '1': # n4 영역은 1로 구성되어 있음
                        n4 += 1
                        col -= 1
                    while arr[row][col] == '0': # n3 영역은 1로 구성되어 있음
                        n3 += 1
                        col -= 1
                    while arr[row][col] == '1': # n2 영역은 1로 구성되어 있음
                        n2 += 1
                        col -= 1
                    # 배율을 확인하기 위해 가장 작은 값을 찾고 그 값으로 해당 영역을 나눠주면 됨
                    min_n = min(n2,n3,n4)
                    if min_n != 0:
                        code = patterns[(n2 // min_n, n3 // min_n , n4 // min_n)]
                        pwd.append(code)

                        if len(pwd) == 8 :
                            even_sum = sum(pwd[::2])
                            odd_sum = sum(pwd[1::2])

                            if (odd_sum * 3 + even_sum) % 10 == 0:
                                total += even_sum + odd_sum
                            else:

patterns = {

}



t = int(input())
for tc in range(1,t+1):
    # n : 세로, m : 가로
    n, m = map(int, input().split())
    # n * m 의 배열에는 16진수가 들어있음
    # 2진수로 변환
    arr = [''] * n # 변환한 2진수를 저장할 리스트
    for i in range(n):
        temp = input()
        bit = ''
        for j in range(m): # 한 개씩 문자를 읽어옮
            # temp[j] # 16진수 => 2진수로 바꿔야 함
            val = f'{int(temp[j],base=16):04b}' # 2진수 문자 변환 완료
            bit += val
        arr[i] = bit # 한 줄씩 16진수를 2진수로 변환된 문자열이 저장됨

    res = scanner(arr)
    print(f'#{tc} {res}')