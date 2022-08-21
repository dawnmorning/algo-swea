student_num = int(input())
pick = list(map(int,input().split()))
modify = []
for i in range(student_num):
    modify.insert(i-pick[i],i+1)
for i in range(len(modify)):
    print(modify[i],end = ' ')