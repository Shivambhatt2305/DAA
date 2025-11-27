text = input("Enter text: ")
pattern = input("Enter pattern: ")

n = len(text)
m = len(pattern)

print("Pattern found at positions:", end=" ")

for i in range(n - m + 1):
    j = 0
    while j < m and text[i + j] == pattern[j]:
        j += 1

    if j == m:
        print(i, end=" ")
