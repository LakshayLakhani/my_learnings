# Examples:
# Input:
# 2
# 6
# 1 2 3 4 5
# 5 90
# 6
# 1 2 3 4 5
# 2 90
#
# Output:
# 1 2 3 4 5 90
# 1 2 90 3 4 5



def insert_element(arr, sizeOfArray, index, element):
    a = sizeOfArray
    i = index
    while i <= sizeOfArray:
        arr.insert((i+1), arr[i])
        i += 1

    arr.insert(i, element)

    return arr


arr = [1,2,3,4,5]
sizeOfArray = 6
index = 2
element = 90



print(insert_element(arr, len(arr), index, element))