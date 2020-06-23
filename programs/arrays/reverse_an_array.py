a = [1,2,3,4,5,6]

b = 0
c = len(a)-1

while b < c:
    a[b], a[c] = a[c], a[b]
    c = c-1
    b = b+1

print(a)

while i < len(arr):
    if arr[i] != arr[res-1]:
        arr[res] = arr[i]
        res +=1
    i += 1


