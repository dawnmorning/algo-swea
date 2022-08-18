import sys
sys.stdin = open('4866.txt')
t = int(input())
for tc in range(1, t+1):
    test = input()
    test_li=[0]
    for i in test:
        if i == '{':
            test_li.append(i)
        elif i == '}':
            if test_li[-1] == '{':
                test_li.pop()
            else:
                result = 0
                break
        if i == '(':
            test_li.append(i)
        elif i == ')':
            if test_li[-1] == '(':
                test_li.pop()
            else:
                result = 0
                break
    else:
        if test_li == [0]:
            result = 1
        else:
            result = 0
    print(f'#{tc} {result}')
