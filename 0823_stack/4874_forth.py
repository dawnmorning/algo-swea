# import sys
# sys.stdin = open('4874.txt')
t = int(input())
for tc in range(1, t+1):
    n = list(map(str, input().split()))
    stack = []
    # n안의 것이 숫자면 stack에 담기
    for i in range(len(n)):
        if n[i].isdigit():
            stack.append(n[i])
        else:
            if n[i] == '.':
                if len(stack) == 1:
                    print(f'#{tc}',*stack)
                    break
                else:
                    print(f'#{tc} error')   # 경우의 수가 너무 많다.. 내가 고3인가?
                    break

            # 두개부터  pop 이후 연산 가능하므로
            if len(stack) > 1:
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                if n[i] == '+' :
                    stack.append(n2 + n1)
                if n[i] == '-':
                    stack.append(n2 - n1)
                if n[i] == '/':
                    stack.append(n2 // n1)
                if n[i] == '*':
                    stack.append(n2 * n1)
            else:
                print(f'#{tc} error')
                break


