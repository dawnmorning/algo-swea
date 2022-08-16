import sys
sys.stdin = open('1216.txt')
for tc in range(1, 11):
    tc = int(input())
    N = 100
    result = 1

    #가로줄 확인
    Garo= []
    for i in range(N):
        Data = input()
        Garo.append(Data)
        #회문 길이
        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if Data[k:M+k] == Data[k:M+k][::-1]:
                    if len(Data[k:M+k]) > result:
                        result = len(Data[k:M+k])

    #세로줄 확인
    Sero = []
    Sero_2 = ''
    for x in range(N):
        for y in Garo:
            Sero_2 += y[x]
        Sero.append(Sero_2)
        Sero_2 =''

    for sero_data in Sero:
        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if sero_data[k:M+k] == sero_data[k:M+k][::-1]:
                    if len(sero_data[k:M+k]) > result:
                        result = len(sero_data[k:M+k])
    print(f'#{tc} {result}')
