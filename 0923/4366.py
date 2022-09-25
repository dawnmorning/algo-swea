import sys
sys.stdin = open('4366.txt')

t = int(input())
for tc in range(1, t+1):
    binary = input()
    triple = input()
    binary_pot = []
    for i in range(len(binary)):
        binary_temp = list(binary)
        if binary_temp[i] == '0':
            binary_temp[i] = '1'
            binary_pot.append(int(''.join(binary_temp),2))
        else:
            binary_temp[i] = '0'
            binary_pot.append(int(''.join(binary_temp), 2))

    triple_pot = []
    for i in range(len(triple)):
        triple_temp = list(triple)
        if triple_temp[i] == '0':
            triple_temp[i] = '1'
            triple_pot.append(int(''.join(triple_temp),3))
            triple_temp[i] = '0'
            triple_temp[i] = '2'
            triple_pot.append(int(''.join(triple_temp),3))
        if triple_temp[i] == '1':
            triple_temp[i] = '2'
            triple_pot.append(int(''.join(triple_temp),3))
            triple_temp[i] = '1'
            triple_temp[i] = '0'
            triple_pot.append(int(''.join(triple_temp),3))
        else:
            triple_temp[i] = '1'
            triple_pot.append(int(''.join(triple_temp),3))
            triple_temp[i] = '2'
            triple_temp[i] = '0'
            triple_pot.append(int(''.join(triple_temp),3))
    value = 0
    for i in binary_pot:
        if i in triple_pot:
            value = i
    print(f'#{tc} {value}')
