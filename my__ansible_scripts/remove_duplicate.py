l = [10, 20, 20, 20, 30, 30]
n = len(l)
res = 1
for i in range(1, n):
  if l[i] != l[i-1]:
    l[res] = l[i]
    res += 1

print(l)