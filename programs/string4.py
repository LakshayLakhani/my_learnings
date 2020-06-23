#Given 2 strings , check if they are

text = "ababab"
pat = "abab"

n = len(text)
m = len(pat)

print(n-m)

for i in range(n-m):
    for j in range(m):
        if text[i+j]!= pat[j]:
            break;
    if j == m:
        print(i)