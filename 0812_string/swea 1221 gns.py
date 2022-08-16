import sys
sys.stdin = open('1221.txt')
t = int(input())
# pattern = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# for tc in range(1,t+1):
#     a, b=input().split()
#     b = int(b)
#     text = list(input().split())
#     length = len(pattern)
#     li = []
#     for i in range(length):
#         for j in range(b):
#             if pattern[i] == text[j]:
#                 li.append(text[j])
#     print(f'#{tc}', *li)
for _ in range(1, t+1):
    tc, N = input().split()
    words = input().split()
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = ''
    for num in numbers:
        for word in words:
            if word == num:
                result += word + ''
    print(f'{tc} {result}')