# arr = [1, 8, 30, -5, 20, 7]
#
# # arr = [5,-10,6,90,3]
#
# k = 3
#
# # o/p = 45
# #O(n.k)
#
# len_arr = len(arr)
#
# res = 0
#
# for i in range(len_arr-k):
#     sum = 0
#     for j in range(i, i+k):
#         sum += arr[j]
#
#     res = max(res, sum)
#
#
# print("res ++++++++++++++++++++++")
# print(res)

# O(n) solution

# arr = [1, 8, 30, -5, 20, 7]

# arr = [5, -10, 6, 90, 3]
#
# k = 2
# len_arr = len(arr)
#
# first_sum = 0
#
# for i in range(0, k):
#     first_sum += arr[i]
#
# res = 0
# for i in range(1, len_arr-k):
#     first_sum = first_sum - arr[i-1] + arr[i+k-1]
#     res = max(res, first_sum)
#
# print("first sum +++++++++++++++++++++++++")
# print(res)








