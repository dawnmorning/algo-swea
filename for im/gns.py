import sys
sys.stdin = open('GNS_test_input.txt')
t = int(input())
for _ in range(1, t+1):
    check = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    out_put=[]
    trash, n = map(str,input().split())
    n = int(n)
    planet = list(map(str,input().split()))
    for i in range(len(check)):
        for j in range(len(planet)):
            if check[i] == planet[j]:
                out_put.append(planet[j])
    print(f'{trash}')
    for j in out_put:
        print(j,end=' ')
    print()