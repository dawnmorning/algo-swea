# import sys
# sys.stdin = open('input.txt')

for tc in range(1,11): #문제의 개수
    cnt = int(input()) #빌딩 수
    building_list = list(map(int, input().split()))
    result = 0 #최종 결과 저장하는 부분
    for i in range(cnt):
        cur_building = building_list[i] #빌딩 목록에서 현재 빌딩 높이

        if not cur_building : #빌딩이 없는 경우
            continue  #다음 값을 볼 수 있게 넘김
        else:
            #좌 우 4개의 빌딩 중 가장 높은 빌딩을 찾는 부분
            max_height = 0
            idx = [-2, 1, 1, 2] #좌, 우 2칸 idx
            for side in range(4): #좌, 우 2칸씩 총 4번비교
                if building_list[i + idx[side]] > max_height: #가장 높은 빌딩
                    max_height = building_list[i + idx[side]]

            if cur_building > max_height: #현재 빌딩과 가장 높은 좌우 빌딩과 비교
                result += cur_building - max_height
    print(f'#{tc} {result}')


