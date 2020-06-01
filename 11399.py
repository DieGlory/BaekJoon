count = int(input())
wait = list(map(int,input().split()))
wait.sort()
result=0
for i in range(count):
    for j in range(i+1):
        result+=wait[j]
print(result)