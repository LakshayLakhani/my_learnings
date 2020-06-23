import math
string = "STRING"
n = len(string)
mul = math.factorial(n)
count = [0 for i in range(256)]

for i in range(0, n):
    count[ord(string[i])] += 1

for i in range(1, 256):
    count[i] = count[i] + count[i-1]

for i in range(n):
    mul = mul/(n-i)
    rank = rank + count[ord(string[i])-1] * mul

for

print("count +++++++++++++++++++++++++++++")
print(count)

