kind, target = map(int,input().split())
kinds = [int(input()) for _ in range(kind)]
result = 0
for i in kinds[::-1]:
    if target >= i:
        result+=target//i
        target %= i
print(result)