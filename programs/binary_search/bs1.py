# given a sorted arrray with repititions, find left most index of an element.

arr = [2, 3, 3, 3, 3]
l = 0
h = len(arr)
search = 3

def binary_search(arr, l, h, search):
    mid = l+h//2
    if search == arr[mid] and (mid == 0 or arr[mid-1] != search):
        return mid
    elif search <= arr[mid]:
        return binary_search(arr, l, mid, search)
    # else search > arr[mid]:
    else:
        return binary_search(arr, mid, h, search)


print(binary_search(arr, l, h, search))

