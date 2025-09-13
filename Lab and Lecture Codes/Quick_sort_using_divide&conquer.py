import math
def partition(arr,low,high):
    pivot=arr[high]
    pIndex=low
    for j in range(low,high):
        if arr[j] <= pivot:
            arr[j], arr[pIndex]=arr[pIndex],arr[j]
            pIndex += 1
    arr[high], arr[pIndex]=arr[pIndex], arr[high]
    return pIndex

def QuickSort(arr,low,high):
    if low < high:
        pi = partition(arr, low, high)
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)
        
arr=[1,8,9,2,3]
QuickSort(arr,0,len(arr)-1)
print(arr)