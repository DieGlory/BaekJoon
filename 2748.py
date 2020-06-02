import sys
count = int(sys.stdin.readline())
if count==0:
    print('0')
else:
    n,m = 0,1
    for j in range(count-1):
        temp=n+m
        n=m
        m=temp
    print(m)


