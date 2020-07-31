count = int(input())
target=[]
stack=[]
result=[]
index = 0
for i in range(count):
    n = int(input())

    for i in range(index,n):
        stack.append(i+1)
        result.append("+")
    
    if index < n:
        index = n

    while stack and stack[-1] == n:
        stack.pop()
        result.append("-")
        continue

if stack:
    print("NO")
else:
    print(*result,sep="\n")