x = '2'
print('16진수 :', x)
y = int(x, base=16)
print(y)  # base의 기본 값은 10
# base는 입력 받는 문자의 진수를 표현
z = f'{y:04b}'
# print(bin(y)) # 0b10
print(f'2진수 : {z}')