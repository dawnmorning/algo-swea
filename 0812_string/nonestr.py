def itoa(n):
    #음수인지 판단
    neg = False #flag : 음수라면 True, 양수라면 False
    if n <0 :
        neg = True
        n = -n
    result = ''
    while n:     #0일때 까지
        n, remain = n // 10, n % 10
        result = chr(ord('0') + remain) + result #역순배열을 막기 위해 result + A가 아니라 A + result
    if neg:  #neg == True의 의미
        return '-' + result
    else:
        return result

print(itoa(1234))
print(itoa(-1234))
