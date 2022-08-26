short_li = []
for _ in range(9):
    short = int(input())
    short_li.append(short)
for i in range(1<<9):
	length = 0
	total =0
	short_tall = []
	for j in range(9):
			if i & (1 << j):
					short_tall += [short_li[j]]
					total += short_li[j]
					length += 1
	if length == 7 and total == 100:
			break
short_tall.sort()
for k in short_tall:
		print(k)