s = 'Reverse This String'
for i in range(len(s)-1,-1,-1):
    print(s[i], end= '')

list_s = list(s)
for idx in range(len(s) // 2):
    list_s[idx], list_s[-1-idx] = list_s[-1-idx], list_s[idx]
print(''.join(list_s))



