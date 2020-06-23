arr = [1, 4, 20, 3, 10, 5]

sum = 33

len_arr = len(arr)

check_sum = 0
new_array = []

for i in range(len_arr):
    if arr[i] == sum:
        print("True")
    if check_sum < sum:
        check_sum += arr[i]
        new_array.append(arr[i])
    if  check_sum > sum:
        break;

print(new_array)

len_new_array = len(new_array)

for i in range(len_new_array):
    check_sum = check_sum - new_array[i]
    print("check sum _+++++++++++++++++++++++")
    print(check_sum)
    if check_sum >= sum:
        print("new array ++++++++++++++++++++++")
        print(new_array[i])
        # new_array.remove(new_array[i])
        # del new_array[i]
        print(new_array)
    else:
        break;

# print("new_array +++++++++++++++++++++")
# print(new_array)





#
#

