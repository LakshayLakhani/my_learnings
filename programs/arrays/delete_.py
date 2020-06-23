arr = [3,8,12,5,6]
x =  12
op = [3,8,5,6]

for i in range(len(arr)):
    if arr[i] == 12:
        l = i
        break;

# print(l)
# print(len(arr))
#


for i in range(l, len(arr)-1):
    print(arr[i])
    arr[i] = arr[i+1]
print(arr)