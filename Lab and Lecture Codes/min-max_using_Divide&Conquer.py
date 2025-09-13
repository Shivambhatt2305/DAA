def minmax(arr):
    mid=len(arr) // 2
    if len(arr) == 1:
        return arr[0], arr[0]
    
    l_min, l_max = minmax(arr[:mid])
    r_min, r_max = minmax(arr[mid:])
    return min(l_min, r_min), max(l_max, r_max)

arr = [1, 2, 3, 4, 5]
min_val, max_val = minmax(arr)
print("Minimum value:", min_val)
print("Maximum value:", max_val)