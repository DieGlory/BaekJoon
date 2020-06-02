import sys
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    m = n*2
    result = [False,False]+[True] * m
    for i in range(2,int(m**0.5)+1):
        if result[i] == True:
            for j in range(i+i,m+1,i):
                result[j] = False
    print(result[n+1:m+1].count(True))
