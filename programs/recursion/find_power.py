def power(n, p):
    if p < 2:
        return n
    p -= 1
    return n * power(n, p)

print(power(2,9))

# def power(n, p):
#     if p < 1:
#         return 1
#     p = p-1
#     power(n, p)
#
#     print("n ++++++++++++++++++++++")
#     print(n)
#
#     print("p ++++++++++++++++++++++")
#     print(p)
#
#     n = n*p
#
#     print("new n ++++++++++++++++++++++++++++")
#     print(n)
#
#     return n
#
# print(power(2, 9))
#
