# # range = (5,10)
#
# arr = [10, 5, 6, 3, 20, 9, 40]
#
# a = []
# b = []
# c = []
#
# for i in range(len(arr)):
#     if arr[i] < 5:
#         a.append(arr[i])
#     elif arr[i] >= 5 and arr[i] <= 10:
#         b.append(arr[i])
#     else:
#         c.append(arr[i])
#
# print(a)
#
# print("b+++++++++++++++")
# print(b)
#
# print("c+++++++++++++")
# print(c)
#
#     # elif arr[i] > 10:
#     #     c.append(arr[i])
#     # else:
#     #     for j in range(5, 10+1):
#     #         if i > j or i < j or i == j :
#     #             b.append(arr[i])
#     #             break;
#     #
#
# d = a + b + c
#
# print("d ++++++++++++++++++++++")
# print(d)
#
#

#lumat partition .

# arr = [-1, -2 , 4, -3, 4, 9, 7]
arr = [1,5,6,2,10,15,17]
# arr = [0,1,2,0,1,2,0,1,1,2]
n = len(arr)

j = 0, 1, 2, 3, 4, 5, 6
i = 0, 1, 2, 3, 4, 4, 5
# arr =[-1, -2,  4, -3, 4 , 7, 9, -8  ]
def partition(arr, low, high): #j = 0, 1, 2, 3, 4, 5, 6, 7
    # pivot                    #i = 0, 1, 1, 2, 2, 2, 2, 3
                               #arr =[-1, -2, -3, 4, ]
    # pivot = arr[high-1] #7
    pivot = 0
    i = (low - 1)
    a = (low - 1)
    b = (low - 1)

    for j in range(low, high+1):
        # If current element is smaller than or
        # equal to pivot
        if (arr[j] < 5):
        # if (arr[j] % 2 == 0):
            # increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        if (arr[j] >= 5 and arr[j] <= 10):
            a += 1
            arr[a], arr[j] = arr[j], arr[a]

        if (arr[j] > 10):
            b += 1
            arr[b], arr[j] = arr[j], arr[b]
#
    # arr[i + 1], arr[high-1] = arr[high-1], arr[i + 1]
    arr[a + b], arr[high-1] = arr[high-1], arr[a + b]


    # return (i + 1)
    return arr

print(partition(arr, 0, n-1))


# def partition(arr, low, high): #j = 0, 1, 2, 3, 4, 5, 6, 7
#     # pivot                    #i = 0, 1, 1, 2, 2, 2, 2, 3
#                                #arr =[-1, -2, -3, 4, ]
#     # pivot = arr[high-1] #7
#     pivot = 0
#     i = (low - 1)
#     a = (low - 1)
#     b = (low - 1)
#
#     for j in range(low, high+1):
#         # If current element is smaller than or
#         # equal to pivot
#         if (arr[j] == 0):
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#         if (arr[j] == 1):
#             a += 1
#             arr[a], arr[j] = arr[j], arr[a]
#
#         if (arr[j] == 2):
#             b += 1
#             arr[b], arr[j] = arr[j], arr[b]
#
#     print("a ++++++++++++++++++++++++++++")
#     print(a)
#
#     print("b+++++++++++++++++++++++++++")
#     print(b)
#
#     print("i++++++++++++++++++++++++++++++")
#     print(i)
#
#     print("arr 1 +++++++++++++++++++++++++++++")
#     print(arr[high])
#     # arr[i + 1], arr[high-1] = arr[high-1], arr[i + 1]
#     arr[a + b], arr[high] = arr[high], arr[a+b]
#
#     # return (i + 1)
#     return arr
#
#
# print("hello +++++++++++++++++++++++++++++")
# print(partition(arr, 0, n-1))

