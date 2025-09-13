#LInear Search Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

def linear_search(arr, target):
    if(target in arr):
        return arr.index(target)
    else:
        return -1

arr=[1, 2, 3, 4, 5]
target=3
result=linear_search(arr, target)
if result!=-1:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found in the array")


# Write code for counting the occurance of a key in a list

# def count_occurrences(lst, key):
#     count = 0

#     for item in lst:
#         if item == key:
#             count += 1

#     return count

# lst = [1, 2, 3, 4, 5, 3, 6]
# key = 3
# occurrences = count_occurrences(lst, key)
# print(f"Key {key} occurs {occurrences} times in the list.")


# # Identify the number of times a key occuring in odd indices

# def count_odd_index_occurrences(lst, key):
#     count = 0
#     for i in range(1, len(arr1)):
#         if i % 2 != 0 and lst[i] == key:
#             count += 1
        
#     return count

# arr1 = [1, 2, 3, 4, 5, 3, 6]
# key = 3
# odd_index_occurrences = count_odd_index_occurrences(arr1, key)
# print(f"Key {key} occurs {odd_index_occurrences} times at odd indices in the list.")