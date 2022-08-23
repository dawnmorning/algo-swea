def step1(inOrder):
    # isp = {'+' :1, '*':2, '(':0}
    # icp = {'+' :1, '*':2, '(':3}
    order = {'+' :1, '*':2 }
    st = []
    postOrder = []
    for token in inOrder:
        if token.isdigit(): #숫자면
            postOrder.append(token)  #추가
        # elif token == "(":
        #     while st and st[-1] != '(': #st에 데이터 있는 동안
        #         postOrder.append(st.pop())
        else:
            #왼쪽 괄호가 있는 경우
            # while len(st) > 0 and isp[st[-1]] >= icp[token]
            # if 스택에 있는 거랑 token이랑 우선순위를 생각
            while len(st) > 0 and order[st[-1]] >= order[token]:
                postOrder.append(st.pop())
            st.append(token)
    while st:
        postOrder.append(st.pop())

            # if len(st) and order[st[-1]] < order[token]: #스택의top의 연산자보다 우선순위가 높으면
            #     st.append(token)
            # else:                                         #그렇지 않으면 top의 연산자의 우선순위가 토큰 우선순위보다
            #     while order[st[-1]] >= order[token]:      #작을 때까지 스택에서 pop한 후 토큰의 연산자를 push
            #         postOrder.append(st.pop())
            #     st.append(token)
    return postOrder   # 받아서 post로

def step2(postOrder):
    st = []   # 위와 서로 다른 스택
    result = 0
    for token in postOrder:
        if token.isdigit():
            st.append(int(token))
        else: # pop한 2개 꺼내서 연산
            v1 = st.pop()
            v2 = st.pop()
            if token == "+":
                st.append(v1+v2)
            else:
                st.append(v1*v2)
    return st[-1]
     #받아서 result에 하나만

t = 10
for tc in range(1, t+1):
    n = int(input())
    inputS = input()

    postOrder = step1(inputS)

    result = step2(postOrder)

    print(f'#{tc} {result}')