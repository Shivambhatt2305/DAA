def binary_search(arr, target):
    if len(arr) == 0:
        return 0
    
    mid = len(arr)// 2
    if mid==1:
        return arr[mid]
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr[:mid], target)
    elif arr[mid]<target:
        return binary_search(arr[mid+1:], target)
    else:
        return -1
    
arr=[1,2,3,4,5,6,7]
target = 3
print(binary_search(arr, target))