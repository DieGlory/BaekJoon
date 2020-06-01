count = int(input())
stack=[]
for i in range(count):
    temp = input()
    while True:
        if '()' in temp:
            temp = temp.replace('()','')
        elif '(' in temp or ')' in temp or ')(' in temp:
            print('NO')
            break
        elif len(temp) == 0:
            print('YES')
            break