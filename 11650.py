array =[]
count = int(input())
for i in range(count):
    array.append(list(map(int,input().split())))
array.sort()
for i in array:
    print(i[0],i[1])