num = int(input())
result = 0

for i in range(1,num):
    string_num = str(i)
    temp = 0

    for j in string_num:
        temp += int(j)

    temp += i

    if temp == num:
        result = i
        break

print(result)


