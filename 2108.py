import sys
from collections import Counter

N = int(input())
numbers=[]
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

#산술평균
def am(nums):
    return round((sum(nums)/N))
#중앙값
def median(nums):
    mid = nums[len(nums)//2] # nums의 개수는 홀수
    return mid
#최빈값
def mode(nums):
    if N == 1:return nums[0]
    c=Counter(nums).most_common(2)
    return (c[1][0] if c[0][1] == c[1][1] else c[0][0])
#범위
def r(nums):return nums[N-1]-nums[0]

numbers.sort()
print(am(numbers))
print(median(numbers))
print(mode(numbers))
print(r(numbers))