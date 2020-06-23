arr = [1,2,3,4]

len_arr = len(arr)

def return_n_1(arr, n):
    if n < 0:
        return

    print(arr[n])

    n -= 1

    return return_n_1(arr, n)

return_n_1(arr, len(arr)-1)