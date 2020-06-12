num = int(input())
array=[]
for i in range(num):
    name = input()[:1]
    array.append(name)
result=[]
for i in sorted(list(set(array))):
    if array.count(i)>=5:
        result.append(i)
if len(result) == 0:
    print("PREDAJA")
else:
    print(*result,sep='')