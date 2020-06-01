formula = input()
result=0
sen = formula.split('-')
if len(sen)>1:
    for i in range(len(sen)):
        if "+" in sen[i]:
            temp =list(map(int, sen[i].split("+")))
            if i == 0:
                result += sum(temp)
            else:
                result -= sum(temp)
        else:
            if i == 0:
                result += int(sen[i])
            else:
                result -= int(sen[i])
else:
    for i in range(len(sen)):
        if "+" in sen[i]:
            temp = list(map(int, sen[i].split("+")))
            if i == 0:
                result += sum(temp)
        else:
            result += int(sen[i])
print(result)