def perm():
    if len(s) == n:
        for i in s:
            print(i, end = ' ')
        print()
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            s.append(i)
            perm()
            s.pop()
            visited[i] = False


n = int(input())
s = []
visited = [False] * (n+1)
perm()