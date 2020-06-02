n = int(input())
m = int(input())
result=[]
for i in range(n,m+1):
    for j in range(2,i+1):
        if i == j:
            result.append(i)
        elif i / j == i // j:
            break
if len(result)==0:
    print(-1)
else:
    print(sum(result))
    print(min(result))