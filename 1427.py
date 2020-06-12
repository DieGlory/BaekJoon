num = list(map(int,list(input())))
num.sort(reverse=True)
print(*num,sep='')