arr = [1, 10, 20, 40, 50, 70, 80]
l = 0
h = len(arr)
search = 80

def binary_search(arr, l, h, search):
    mid = l+h//2

    if search == arr[mid] :
        return mid
    elif search > arr[mid]:
        return binary_search(arr, mid, h, search)
    else:
        return binary_search(arr, l, mid, search)

print(binary_search(arr, l, h, search))

