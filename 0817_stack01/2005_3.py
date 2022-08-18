import sys
sys.stdin = open('2005.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    pascal = [1]   #초기 값을 설정한 pascal(이전 결과를 담고 있는 역할

    for _ in range(1, n): #이미 첫번재 라인은 초기값으로 생성했기에 1부터 시작함
        my_pascal = []
        my_pascal.append(1) #왼쪽 끝에 1추가

        #중간은 이전 줄의 좌우 합한 값
        for i in range(len(pascal) - 1):
            my_pascal.append(pascal[i] + pascal[i+1])


        my_pascal.append(1)  #우측 끝에 1 추가
        pascal = my_pascal #현재 계산한 값을 이전 파스칼에 저장
        print(*pascal)