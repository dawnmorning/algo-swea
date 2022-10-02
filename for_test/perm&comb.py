from itertools import permutations

li = [1, 2, 3]
r = 2
for i in permutations(li,2):
    for j in list(i):
        print(j)

