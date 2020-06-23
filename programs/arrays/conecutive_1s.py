# arr = [0,1,1,0,1,0]
op = 2

arr = [1,1,1,1]
# op = 4
#
# arr = [0,0,0]
# op = 0
#
# arr = [1,0,1,1,1,1,0,1,1]
# op = 4

# k = []
# count = 0
#
# k = {}
# v = 1
#
# for i in arr:
#     if i == 1:
#         count += 1
#
#     if i == 0:
#         # k.append(count)
#         k[v] = count
#         count = 0
#         v += 1
#
#     # k.append(count)

# print("k +++++++++++++++++++++++")
# print(k)

# arr = [0,1,1,1,0,1,1]

# arr = [1,1,1,1]
arr = [1,0,1,1,1,1,0,1,1]
k = []
max_count = 0
count = 0
for i in arr:
    if i == 1:
        count +=1

    if i == 0:
        # max_count = max(max_count, count)
        count = 0

    max_count = max(max_count, count)


print(max_count)