num = []
for _ in range(9):
    num.append(int(input()))
s = sum(num)
ss = [True] * 9

for i in range(9):
    for j in range(i+1,9):
        if (s-(num[i]+num[j])) == 100:
            ss[i] = False
            ss[j] = False
            

for i in range(9):
    if ss[i]:
        print(num[i])

