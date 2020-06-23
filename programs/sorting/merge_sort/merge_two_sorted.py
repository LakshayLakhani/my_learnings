# a = [10, 15, 20, 40]
# b = [5, 6, 6, 10, 15]

# a = [1,1,2]
# a=[3,5,6,7,4,8,10]
# b = [3]

a=[3,4,5,6,7,8,10]
b=[4,5,10,10]
d = []
e = 0
f = 0

len_a = len(a)
len_b = len(b)

while e < len_a and f< len_b:
    if a[e] < b[f]:
        d.append(a[e])
        e += 1
    else:
        d.append(b[f])
        f += 1

while e < len_a:
    d.append(a[e])
    e += 1

while f < len_b:
    d.append(b[f])
    f += 1

print(d)
