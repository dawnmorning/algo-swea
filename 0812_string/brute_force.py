
def bruteforce(pattern, text):
    m = len(pattern)
    n = len(text)

    for i in range(n - m+1): #패턴길이가 텍스트 길이 넘어가기전까지만 봐도 됨
        for j in range(m): #패턴의 길이만큼 돌면 됨
            if pattern[j] != text[i]:
                break  # 가장 가까운  for와 관련
        else: #패턴이 매칭된 상태
            return i
    else:
        return -1 #탐색 실패시
text = 'I am JH'
pattern = 'JH'
print(bruteforce(pattern, text))