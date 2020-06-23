# array = [1,2,3,4,5]
# n = 0
#
# def search_n(array, n):
#     if n < len(array):
#         if array[n] == 3:
#             print(array)
#             return True
#         else:
#             n += 1
#             search_n(array, n)
#
# print(search_n(array, n))

#another method
array = [1,2,3,4,5]
x = 3
l = 0
r = len(array)-1

def search(l, r, x, array):
    if r < l:
        return False
    if array[l] == x:
        return True
    if array[r] == x:
        return  True
    return search(array, l+1, r-1, x)

search(l, r, x, array)








