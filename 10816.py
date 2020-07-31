from collections import Counter

input()
n = list(map(int,input().split()))
n_dict = Counter(n)
input()
r = list(map(int,input().split()))
result=[]
for i in r:
    result.append(n_dict[i])
print(*result)