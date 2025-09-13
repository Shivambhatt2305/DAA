def merge(arr):
    if(len(arr)<=1):
        return arr
    mid=len(arr)//2
    left=merge(arr[:mid])
    # merge(left)
    right=merge(arr[mid:])
    # merge(right)
    return merge_sort(left,right)

def merge_sort(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr=[1,2,9,6,23]
print(merge(arr))