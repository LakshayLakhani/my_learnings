# iterative way
# count = 0
# n = 123456
#
# while n>0:
#     count += 1
#     n = n//10
#
# print(count)

##  recursive way

# def count(n):
#     if n <= 0:
#         return 0
#     return 1 + count(n//10)
#
# print(count(123456))