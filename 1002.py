count = int(input())

for i in range(count):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    distance = ((x2-x1)**2+(y2-y1)**2)**0.5

    if distance == 0 and r1 == r2:
        print(-1)
    elif distance == 0 and r1 > r2:
        print(0)
    elif distance == 0 and r2 > r1:
        print(0)
    elif distance+r1 < r2 or distance+r2 <r1:
        print(0)
    elif distance+r1 == r2 or distance+r2 == r1:
        print(1)
    elif distance == r1+r2:
        print(1)
    elif distance > r1+r2:
        print(0)
    elif distance +r1 > r2 or distance +r2 > r1:
        print(2)
    elif distance <r1+r2:
        print(2)