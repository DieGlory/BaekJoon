num = int(input())
num_list =list(map(int,input().split()))
result=0
for i in num_list:
    for j in range(2,i+1):
        if i == j:
            result+=1
        elif i / j == i // j:
            break
print(result)