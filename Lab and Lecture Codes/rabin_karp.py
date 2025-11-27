text = input("Enter text: ")
pattern = input("Enter pattern: ")

n = len(text)
m = len(pattern)

d = 256      # number of characters
q = 101      # prime number for hashing

h = 1
for i in range(m - 1):
    h = (h * d) % q

p = 0   # hash for pattern
t = 0   # hash for text window

for i in range(m):
    p = (d * p + ord(pattern[i])) % q
    t = (d * t + ord(text[i])) % q

print("Pattern found at positions:", end=" ")

for i in range(n - m + 1):

    if p == t:
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            print(i, end=" ")

    if i < n - m:
        t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
        if t < 0:
            t += q
