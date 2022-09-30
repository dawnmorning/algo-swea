def SelectionSort(A):
    n = len(A)
    for i in range(n-1):
        minV = i
        for j in range(i+1,n):
            if A[j] < a[minV]:
                minV = j
            A[minV], A[i] = A[i], A[minV]