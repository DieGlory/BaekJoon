result = []
for i in range(5):
    result.append(sum(list(map(int,input().split()))))
print(result.index(max(result))+1,max(result))
