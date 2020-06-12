num = int(input())
for i in range(num):
    result=[]
    pointer = 0
    pwd = input()
    for j in pwd:
        if j == "<":
            if pointer>0:
                pointer-=1
            else:
                pointer=0
        elif j == '>':
            if pointer>len(result):
                pass
            else:
                pointer+=1
        elif j == '-':
            if pointer>0:
                result.pop(pointer-1)
            else:
                pass
        else:
            result.insert(pointer,j)
            pointer+=1
    print(*result,sep='')