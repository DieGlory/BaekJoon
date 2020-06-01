count = int(input())

for x in range(count):
    h,w,n = map(int,input().split())
    array =[]
    for x in range(1,w+1):
        inner_array=[]
        for y in range(1,h+1):
            temp=""
            temp = str(y)
            if x < 10:
                temp+="0"
            temp+=str(x)
            array.append(temp)
    print(array[n-1])