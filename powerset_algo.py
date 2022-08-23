# def backtrack(a,k,input):
#     global maxcandidates
#     c = [0] * maxcandidates
#     if k == input:
#         for i in range(1,k+1):
#             print(a[i], end = ' ')
#         print()
#     else:
#         k+=1
#         ncandidates = construct_candidates(a,k,input,c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a,k,input)
# def construct_candidates(a,k,input,c):
#     c[0] = True
#     c[1] = False
#     return 2
# maxcandidates = 2
# nmax = 4
# a = [0] * nmax
# backtrack(a,0,3)

# 좀 더 쉬운 방법

number = list(range(1,6))  # 숫자
selected = [False] * len(number) # 사용 안된 상태 갯수 표시
last_result = []
def powerset(idx): # 몇번째 idx가 선택/선택X 고려하는 부분
    if idx < len(number):   # 사용되는 숫자를 정할 수 있음
        selected[idx] = True # 사용 되었을 때
        powerset(idx + 1)  # 다음자리 확인
        selected[idx] = False # 사용되지 않았을 때
        powerset(idx + 1)
    else:
        # 부분집합을 뽑아내는 곳
        result = []
        for i in range(len(number)):
            if selected[i]:         # 실제로 사용되었다면
                result.append(number[i])

        last_result.append(result)
powerset(0)
print(last_result)