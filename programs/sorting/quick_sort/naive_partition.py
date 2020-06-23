arr = [5, 13, 6, 9, 12, 11, 8]

a = []

m=6

b = []

for i in arr:
    if i <= arr[m]:
        a.append(i)
    else:
        b.append(i)

c = a+b

print(c)
