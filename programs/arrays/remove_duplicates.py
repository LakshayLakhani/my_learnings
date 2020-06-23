arr = [10,20,20,30,30,30]

op = [10,20,30]

# for i in range(len(arr)):
#     print("arr i +++++++++++++++++++++++++++++++++")
#     print(arr[i])
#     # if arr[i] == arr[i-1]:
#     #     arr.remove(arr[i])

i = 1

while i < len(arr):
    if arr[i] == arr[i-1]:
        arr.remove(arr[i])
    i += 1


print("list +++++++++++++++++++++++++")
print(arr)
