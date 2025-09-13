# Selection Sort also known as in-place sorting algorithm
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [4, 5, 3, 1, 2, 8]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)