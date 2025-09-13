def counting_sort_alphabet(arr):
    max_ = max(arr)
    count = [0 for _ in range(26)]
    for char in arr:
        count[ord(char)-ord('a')] += 1
    ans = []
    for i in range(len(count)):
        ans.extend([chr(i+ord('a'))] * count[i])
    return ans

arr=['c','d','a','f','a','w']
print(counting_sort_alphabet(arr))