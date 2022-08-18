def push(item,size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

