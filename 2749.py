import sys
num = int(sys.stdin.readline())
n,m =0,1
for i in range(num-1):
    temp=n+m
    n=m
    m=temp
print(m)
