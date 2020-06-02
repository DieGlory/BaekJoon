import sys
count = int(sys.stdin.readline())
for num in range(count):
    n = int(sys.stdin.readline())
    result = [False,False]+[True] * n
    for i in range(2,int(n**0.5)+1):
        if result[i] == True:
            for j in range(i+i,n+1,i):
                result[j] = False
    s = n//2
    if result[s]:
        print(s,s)
    else:
        for j in range(s,1,-1):
            ss = n-j
            if result[j] and result[ss]:
                print(j,ss)
                break