# permutation

def perm(n,k):
    if n == k :
        print(p)
    else:
        for i in range(k):
            p[n],p[i] = p[i], p[n]
            perm(n+1,k)
            p[n],p[i] = p[i], p[n]

p = [1,3,4]
perm(0,3)

# combination

