n = int(input())

for i in range(n):
    print(" "*(n-(i+1)),end='')
    if i == 0:
        print("*")
    elif 0<i<(n-1):
        print("*",end='')
        print(" " * (2*i-1),end='')
        print("*")
    elif i == (n-1):
        print("*"*(2*n-1))