count = int(input())

for i in range(count):
    print(' '*i+'*'*(count*2-1-i*2))
for i in range(count-1):
    print(' '*(count-2-i)+'*'*(3+2*i))