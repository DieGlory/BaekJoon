array =[]
count = int(input())
for i in range(count):
    array.append(list(input().split()))
array.sort(key=lambda x:int(x[0]))
for i in array:
    print(i[0],i[1])
