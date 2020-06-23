# arr = [[1,3], [2,4], [5,7], [6,8]]
arr = [[7, 9], [6, 10], [4,5], [1,3], [2,4]]
op = [[1,4], [5,8]]

k = []
for i in range(1, len(arr)):
    if arr[i][0] < arr[i-1][1] :
        if arr[i][0] < arr[i-1][0]:
            k.append(arr[i])
        else:
            k.append([arr[i-1][0], arr[i][1]])


print(k)
