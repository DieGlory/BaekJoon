array=[]
for i in range(5):
    temp=int(input())
    if temp<40:
        temp=40
    array.append(temp)
print(int(sum(array)/5))

