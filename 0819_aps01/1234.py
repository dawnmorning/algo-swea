import sys
sys.stdin = open('1234.txt')
t = 10
for tc in range(1, t+1):
    n, value = list(map(str,input().split()))
    n = int(n)
    st= []
    for i in value:
        st.append(i)
    i = 0
    while i + 1 < len(st):
        if st[i] == st[i + 1]:
            st.pop(i + 1)
            st.pop(i)
            i -= 1
        else:
            i += 1
    print(f'#{tc}',end = ' ')
    for i in st:
        print(i, end='')
    print()







