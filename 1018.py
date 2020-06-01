y_len,x_len  = map(int,input().split())
table =[]
for i in range(y_len):
    table.append(list(input()))
# print(table)
result=[]
score_w=0
score_b=0
for y in range(y_len-7):
    for x in range(x_len-7):
        roi = []
        for i in range(8):
            roi.append(table[y+i][x:x+8])
        # print(roi)
        for i in range(8):
            for j in range(8):
                if (i+j)%2==0:
                    if roi[i][j]=="W":
                        pass
                    else:
                        score_w+=1

                    if roi[i][j]=="B":
                        pass
                    else:
                        score_b+=1
                else:
                    if roi[i][j]=="B":
                        pass
                    else:
                        score_w+=1

                    if roi[i][j]=="W":
                        pass
                    else:
                        score_b+=1
        result.append(score_w)
        result.append(score_b)
        score_w = 0
        score_b = 0
print(min(result))

