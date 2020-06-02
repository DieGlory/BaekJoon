import sys

count = int(sys.stdin.readline())
for i in range(count):
    num = int(sys.stdin.readline())
    if num==0:
        print('1 0')
    else:
        n,m = 0,1
        for j in range(num-1):
            temp=n+m
            n=m
            m=temp
        print(n,m)


