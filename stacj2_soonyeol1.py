def f(i,N):
    if i== N:
        print(p)  #순열완성
    else:
        for j in range(i, N): # p[i]에 들어갈 숫자 p[j]결정
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[j], p[i] = p[i], p[j]

p = [1,2,3]
f(0,3)