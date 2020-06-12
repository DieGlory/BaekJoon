def merge_sort(array):
    if len(array) <=1:
        return array
    else:
        mid = len(array)//2
        left_array = array[:mid]
        right_array = array[mid:]
        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)
        return merge(left_array,right_array)

def merge(left,right):
    result = []
    while len(left) >0 or len(right)>0:
        if len(left) >0 and len(right)>0:
            if left[0] >= right[0]:
                result.append(right[0])
                del right[0]
            else:
                result.append(left[0])
                del left[0]
        elif len(left)>0:
            result.append(left[0])
            del left[0]
        elif len(right)>0:
            result.append(right[0])
            del right[0]
    return result
array =[]
count = int(input())
for i in range(count):
    array.append(int(input()))
array =merge_sort(array)
print(*array, sep="\n")