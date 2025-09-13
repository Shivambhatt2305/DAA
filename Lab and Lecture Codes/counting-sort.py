def counting_sort(arr): 
    max_val = arr[0] 
    for i in arr: 
        if i > max_val: 
            max_val = i  # Fixed: use i, not arr[i]
 
    count = [0 for _ in range(max_val + 1)] 
    for i in arr: 
        count[i] += 1 
 
    sorted_arr = [] 
    for i in range(len(count)): 
        for _ in range(count[i]): 
            sorted_arr.append(i) 
    return sorted_arr 
 
arr = [6, 1, 1, 8, 3, 3, 1] 
sorted_arr = counting_sort(arr) 
print("Sorted array:", sorted_arr)
