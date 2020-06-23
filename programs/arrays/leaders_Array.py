# ip : arr = [7, 10, 4, 10, 6, 5, 2]
# op : arr = [10, 6, 5, 2]

# ip: arr = [1, 2, 3, 4, 0]
# op: arr = [4, 0]
#
# ip: arr = 7, 4, 5, 7, 3
# op: arr = 3, 7, 7
#
# ip: arr = 4, 1, 4
# op: arr = 4, 4

# O(n**2) solution
# arr = [ 4, 1, 4]
# a = len(arr)-2
# k = [arr[-1]]
# for i in range(a, 0, -1):
#     inital = True
#     for j in range(i+1 , a+1+1):
#         if arr[i] <= arr[j] :
#             inital = False
#             break;
#     if inital == True:
#         k.append(arr[i])
#
# print("k ++++++++++++++++++++++++++++++++++")
# print(k)

# ip : arr = [7, 10, 4, 10, 6, 5, 2]
# op : arr = [10, 6, 5, 2]

#O(n) solution

arr = [7, 10, 4, 10, 6, 5, 2]
len_arr = len(arr)
k = [arr[-1]]

initial = arr[len_arr-1]

for i in range(len_arr-2, 0, -1):
    if arr[i] >= initial:
        initial = arr[i]
        k.append(initial)


print(k)















