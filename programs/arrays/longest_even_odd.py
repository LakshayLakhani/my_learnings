arr = [10, 12, 14, 7, 8]
# op = 3

# ip = [7,10,13,14]
# op = 4
#
# ip = [10, 12, 8, 4]
# op = 1

for arr[i] in range(len_arr):
    if arr[i] % 2 == 0:
        if arr[i+1] %2 != 0:
            print("even odd")

    if arr[i] % 2 != 0:
        if arr[i+1] == 0:
            print("odd even ")
