array =[]
count = int(input())
for i in range(count):
    array.append(input())
array = sorted(list(set(array)))
array.sort(key=lambda x:len(x))
for i in array:
    print(i)
