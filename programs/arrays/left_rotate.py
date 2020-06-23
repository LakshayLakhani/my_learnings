# arr = [1,2,3,4,5]
# op = [2,3,4,5,1]
#
# first = arr[0]
# for i in range(len(arr)-1):
#     arr[i] = arr[i+1]
#
# arr[-1]=first
#
# print(arr)

# O(nd) ->
# arr = [1,2,3,4,5]
#
# d = 3
#
# for i in range(d):
#     first = arr[0]
#     for i in range(len(arr)-1):
#         arr[i] = arr[i+1]
#
#     arr[-1]=first
#
# print(arr)



#
# arr = [1, 2, 3, 4, 5]
# op = [4, 5, 1, 2, 3] #for 3
#
# op = [5, 1, 2, 3, 4] #for 4
#
# d = 4
# diff = len(arr) - d
# len_arr = len(arr)
#
# a = []
#
# # for i in range(diff):
# #     a.append(arr[i])
#
# for i in arr[-diff:]:
#     a.append(i)
#
# for i in range(d):
#     a.append(arr[i])
#
# print(a)

#for 3

# O(n) -> time
#O(1) -> space


# op = [4, 5, 1, 2, 3] #for 3
#
# rev_arr = [5,4,3,2,1]
#
# reverse -> full array
# reverse -> (length - d) array
# reverse -> left 4 array

op = [5, 1, 2, 3, 4]
d = 3

# reverse full array - [5,4,3,2,1]
# reverse length - d array - [5, 4,3,2,1]
# reverse left d arrays - [5, 1,2,3,4]

arr = [1,2,3,4,5]

def reverse(arr):
    i = 0
    b = len(arr)-1
    while i < b:
        arr[i], arr[b] = arr[b], arr[i]
        i += 1
        b -= 1

    return arr

# op = [4, 5, 1, 2, 3] #for 3

def rotate_by_d(arr, d):
    arr = reverse(arr)
    arr = reverse(arr[:len(arr)-d]) + arr[len(arr)-d:]
    arr = arr[:len(arr)-d] + reverse(arr[len(arr)-d:])

    return arr

print(rotate_by_d(arr, d))

















