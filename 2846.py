size = int(input())
array = list(map(int,input().split()))
pointer=0
result=[]
if size==1:
    pass
else:
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            if len(result) > pointer:
                result[pointer]+= array[i+1]-array[i]
            else:
                result.append(array[i+1]-array[i])
        elif array[i] >= array[i+1]:
            if len(result) <= pointer:
                pass
            else:
                pointer+=1
    if result:
        print(max(result))
    else:
        print(0)
