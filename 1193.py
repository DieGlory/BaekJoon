
x = int(input())
under = 0
upper = 1
count = 1
while True:
    if under < x <= upper:
        break
    else:
        count += 1
        under = upper
        upper += count

if count % 2 == 1:
    print(str(1+count-(x-under))+"/"+str(x-under))
else:
    print(str(x - under) + "/" + str(1 + count - (x - under)))