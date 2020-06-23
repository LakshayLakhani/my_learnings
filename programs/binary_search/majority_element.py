# arr = [8, 3, 4, 8, 8]
# op = 0, 3, 4 # any of index 8

# arr = [3, 7, 4, 7, 7, 5]
# op = -1 (No majority)

arr = [20, 30, 40, 50, 50, 50, 50]
# op = 3 or 4 or 5 or 6

d = {}

a = len(arr)/2

print("a ++++++++++++++++++++++++++++")
print(a)

for i in arr:
    if d.get(i, None):
        d[i] += 1
        if d[i] > a:
            # print(arr.index(i))
            break
    else:
        d[i] = 1

print(d)
 b = []
for i in d:
    if d[i] > a:
