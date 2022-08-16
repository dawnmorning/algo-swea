def pre_process(pattern):
    # 전처리를 위한 테이블을 작성(LPS table, longest prefix suffix)
    lps = [0] * len(pattern)
    j = 0 #lps를 만들기 위한 prefix index
    for i in range(1, len(pattern)): # 0번째 자리는 패턴 확인 불필요

        # prefix index 위치에 있는 문자와 비교
        if pattern[i] == pattern[j]:
            lps[i] = j + 1 # i  앞에 중복되는 패턴이 존재한다.
            j += 1 # j는 중복된 글자의 자리수
        else:
            # 비었을 때 바로 0으로 만드는 것이 아니라 0으로 이동한 다음 prefix idx비교를 한 번 더 해야함
            j = 0
            if pattern[i] == pattern[j]:
                lps[i] = j+1
                j += 1
    return lps

def KMP(text, pattern):
    lps = pre_process(pattern) #전처리로 lps테이블 생성

    i = 0  #text index 순회
    j = 0 #pattern index
    while i < len(text):
        if pattern[j] == text[i]:  #같은 문자라면 다음 문자 비교
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == len(pattern):  # pattern이 전부 일치할 때
            return i - j          # text의 위치
    return -1   #일치하지 문장 없는 경우, -1 반환

text = 'ABC ABCDAB ABCDABCDABDE'
pattern = 'ABCDABD'
print(KMP(text, pattern))