# string = "geeksforgeeks"

# string = "abbcc"

# b = False
#
# #O(n2) solution
# for i in range(0, len(string)):
#     for j in range(1, len(string)):
#         if string[i] == string[j]:
#             print("string +++++++++++++++++++++++++")
#             print(i)
#             b = True
#             break;
#
#     if b == True:
#         break;

#O(n) solution

fi = [-1 for i in range(256)]

string = "abccbd"
res = 99999999

for i in range(0, len(string)):
    if fi[ord(string[i])] == -1:
        fi[ord(str[i])] = i
    else:
        res = min(res, fi[ord(str[i])])
        # res = min(res, fi)


if res == 99999999:
    print("-1 ++++++++++++++++++")
else:
    print(res)