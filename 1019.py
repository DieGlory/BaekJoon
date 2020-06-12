import sys
num = int(sys.stdin.readline())
array=[0]*10
def check(num,array):
    if num==1:
        array[num] += 1
        return
elif len(str(num))<2:
        array[num]+=1
        return
    else:
