import sys
n,m = map(int,sys.stdin.readline().split())
result = [False,False]+[True] * m
for i in range(2,int(m**0.5)+1):
    if result[i] == True:
        for j in range(i+i,m+1,i):
            result[j] = False
for i in [i for i in range(n,m+1) if result[i]==True]:
    print(i)
