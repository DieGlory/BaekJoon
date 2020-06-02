x,y=[],[]
for i in range(3):
    tx,ty=map(int,input().split())
    x.append(tx)
    y.append(ty)
roix = list(set(x))
roiy = list(set(y))
for i in range(2):
    if x.count(roix[i]) == 2:
        del x[x.index(roix[i])]
        del x[x.index(roix[i])]
    if y.count(roiy[i]) == 2:
        del y[y.index(roiy[i])]
        del y[y.index(roiy[i])]
print(x[0],y[0])


