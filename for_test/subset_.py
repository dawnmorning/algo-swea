arr = [1, 2, 3]
subsets = [[]]

for num in arr:
    size = len(subsets)
    for a in range(size):
        subsets.append(subsets[a] + [num])
print(subsets)