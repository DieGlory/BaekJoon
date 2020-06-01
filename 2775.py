# def num(k,n):
#     if n==1:
#         return 1
#     elif k==0:
#         return n
#     else:
#         return num(k-1,n) + num(k,n-1)

count = int(input())
for i in range(count):
    k = int(input())
    n = int(input())
    ground_zero = [i for i in range(1, n+1)]
    for i in range(k):
        for j in range(1,n):
            ground_zero[j] += ground_zero[j - 1]
    print(ground_zero[-1])