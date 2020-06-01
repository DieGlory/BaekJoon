count = int(input())

for i in range(count):
    x,y= map(int,input().split())
    distance = y-x
    under,upper = 0,1
    add = 1
    result=0
    while True:
        result += 1
        if under < distance <= upper:
            break
        under = upper
        upper += add
        result += 1
        if under < distance <= upper:
            break
        add+=1
        under = upper
        upper += add
    print(result)
