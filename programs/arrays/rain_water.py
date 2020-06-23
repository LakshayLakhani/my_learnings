# arr = [7, 4, 0, 9]
# op = 10

# arr = [6, 9, 9]
# op = 0

# arr = [7, 4, 0, 9]
# arr = [6,9,9]
# arr = [2,0,2]
# arr = [1,2,3]
# arr = [3,2,1]

# solution 1  #wrong solution
# len_arr = len(arr)
#
# min_value = min(arr[0], arr[-1])
#
# saved_water = 0
#
# for i in range(len_arr-1):
#     if arr[i] < min_value:
#         saved_water += (min_value-arr[i])
#
# print("saved water ++++++++++++++++++++++++")
# print(saved_water)

#solution 2 # O(n) solution .

# arr = [5, 0, 6, 2, 3]
# arr = [7, 4, 0, 9]
# arr = [6, 9, 9]

arr = [3,2,1]

len_arr = len(arr)
lmax = [arr[0]]
rmax = [arr[-1]]

left_max = arr[0]
for i in range(1, len_arr):
    left_max = max(left_max, arr[i-1])
    lmax.append(left_max)

right_max = arr[-1]
for i in range(len_arr-1, 0, -1):
    right_max = max(right_max, arr[i])
    rmax.append(right_max)

rmax = rmax[::-1]

water = 0
for i in range(1, len_arr):
    min_of = min(lmax[i], rmax[i])
    if arr[i] < min_of:
        water += min_of - arr[i]

print("water ++++++++++++ +++++++++++++++++")
print(water)

    # if arr[i] < lmax[] :
    #     water +=


# for i in range(0, len_arr):
#     l_max = arr[i]
#     for j in range(0, i):
#         print("j +++++++++++++++++++")
#         print(j)
#         l_max = min(l_max, arr[j])
#         break;
#     lmax.append(l_max)
#
# print(lmax)
#

    # l_max = arr[i]
    # for j in range(i, ):
    #     print(arr[j])





