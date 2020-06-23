arr = [2, 4, 1, 3, 5]

len_arr = len(arr)
k = []

for i in range(len_arr):
    for j in range(i+1, len_arr):
        if arr[i] > arr[j]:
            k.append((arr[i], arr[j]))


print(k)