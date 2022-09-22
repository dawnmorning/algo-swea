# import sys
# from itertools import permutations
# input = sys.stdin.readline
# sys.stdin = open('11399.txt')
#
# n = int(input())
# time = list(map(int, input().split()))
# time = list(permutations(time,n))
# minV = 99999
# for i in range(len(time)):
#     compare = []
#     value = 0
#     for j in range(n):
#         value += time[i][j]
#         compare.append(value)
#     if minV > sum(compare):
#         minV = sum(compare)
# print(minV)

count = input()
persons = list(map(int, input().split()))
persons.sort()

sum = 0
new = 0
for i in persons:
    new += i
    sum += new

print(sum)
