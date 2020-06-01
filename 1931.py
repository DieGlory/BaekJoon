# kind = int(input())
# kinds = [list(map(int,input().split())) for _ in range(kind)]

howmany=int(input())
time=[[0]*2 for i in range(howmany)]
for i in range(howmany):
    temp=input().split()
    time[i][0]=int(temp[0])
    time[i][1]=int(temp[1])
time.sort(key=lambda x:x[0])
time.sort(key=lambda x:x[1])

start=-1
count=0

for i in range(howmany):
    if time[i][0] >= start :
        count=count+1
        start=time[i][1]
        #time[i][2]=1

#print(time)
print(count)