import sys

def push(stack,item):
    stack.append(item)

def top(stack):
    if len(stack)==0:
        print(-1)
    else:
        print(stack[-1])

def size(stack):
    print(len(stack))

def empty(stack):
    if len(stack)==0:
        print(1)
    else:
        print(0)

def pop(stack):
    if len(stack)>0:
        print(stack[-1])
        del(stack[-1])
    else:
        print(-1)

count = int(sys.stdin.readline())

stack=[]

for i in range(count):
    order = sys.stdin.readline()
    if order.split()[0] == 'push':
        push(stack,order.split()[1])
    elif order.split()[0] == 'pop':
        pop(stack)
    elif order.split()[0] == 'size':
        size(stack)
    elif order.split()[0] == 'empty':
        empty(stack)
    elif order.split()[0] == 'top':
        top(stack)
