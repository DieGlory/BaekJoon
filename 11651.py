array =[]
count = int(input())
for i in range(count):
    array.append(list(map(int,input().split())))
array.sort(key=lambda x: x[0])
array.sort(key=lambda x:x[1])
for i in array:
    print(i[0],i[1])