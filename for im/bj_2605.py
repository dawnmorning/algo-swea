T = int(input())
arr = list(map(int, input().split()))
student_arr = []

for i in range(0, T):
    student_arr.insert(i - arr[i], i + 1) #보낼 위치, 들어갈 값
print (*student_arr)