# ip
a = [2, 5, 8, 13, 15]

b = [1, 3, 8, 15, 18, 20, 25]

len_a = len(a)
len_b = len(b)

e = 0
f = 0

d = []

while e < len_a :
    if a[e] < b[f]:
        e += 1
    elif a[e] == b[f]:
        d.append(a[e])
        e += 1
        f += 1
    else:# a[e] > b[f]:
        f +=1

print(d)

