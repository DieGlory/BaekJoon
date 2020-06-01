count, target = map(int,input().split())
card_num = list(map(int,input().split()))
result=[]
score=0
ans =0
for i in range(count-2):
    for j in range((i+1),count-1):
        for k in range((j+1),count):
            score = card_num[i]+card_num[j]+card_num[k]
            result.append(score)

for i in result:
    if 0<= (target-i)<(target-ans):
        ans = i
# print(result)
# print(len(result))
print(ans)