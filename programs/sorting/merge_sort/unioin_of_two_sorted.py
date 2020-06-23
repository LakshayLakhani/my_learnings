# a = [3, 8, 8, 10, 16, 16, 17, 18, 18, 19]
# b = [2, 8, 9, 10, 15, 15, 15, 15, 15]

# a = [3, 8, 10]
# b = [2, 8, 9, 10, 15]

a = [2, 3, 3, 3, 4]
b = [4, 4]

output = [2, 3, 8, 9, 10, 15]

len_a = len(a)
len_b = len(b)

e = 0
f = 0

d = []

while e < len_a and f < len_b:

    if a[e] == a[e-1] and e > 1:
        e += 1
        continue;

    if b[f] == b[f-1] and f >1:
        f += 1
        continue;

    if a[e] == b[f] :
        d.append(a[e])
        e += 1
        f += 1

    elif a[e] < b[f]:
        d.append(a[e])
        e += 1

    else:
        d.append(b[f])
        f += 1

while e < len_a and e > 1:
    if a[e] != a[e-1]:
        d.append(a[e])
    e += 1


while f < len_b and f > 1 :
    if b[f] != b[f-1] :
        d.append(b[f])
    f += 1


print(d)