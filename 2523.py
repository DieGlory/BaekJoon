count = int(input())

for i in range(count):
    for j in range(i+1):
        print("*",end='')
    print()
for i in range(count-1,0,-1):
    for j in range(i):
        print("*", end='')
    print()