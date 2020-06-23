# Lucky Numbers
# Lucky numbers are subset of integers. Rather than going into much theory, let us see the process of arriving at lucky numbers,
# Take the set of integers
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,……
# First, delete every second number, we get following reduced set.
# 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,…………
# Now, delete every third number, we get
# 1, 3, 7, 9, 13, 15, 19,….….
# Continue this process indefinitely……
# Any number that does NOT get deleted due to above process is called “lucky”.
#
# Your task is to complete isLucky function.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases.
# Then T test cases follow. The first line of each test case contains an integer N.
#
# Output:
# For each testcase, in a new line, print 1 if the given number is a lucky number, else print 0.
#
# Your Task:
# This is a function problem. You only need to complete the function isLucky that takes n as parameter and returns either 0 or 1.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 105
#
# Example:
# Input:
# 2
# 5
# 19
# Output:
# 0
# 1
#
# Explanation:
# Testcase1: 5 is not a lucky number as it gets deleted in the second iteration.
# Testcase2: 19 is a lucky number
#
# ** For More Input/Output Examples Use 'Expected Output' option **

def remove_two(a):
    i = 0
    k = []
    while i < len(a):
        if (i + 1) % 2 != 0:
            k.append(a[i])
        i += 1
    return k


def remove_three(b):
    i = 0
    k = []
    while i < len(b):
         if (i+1) % 3 != 0:
             k.append(b[i])
         i += 1
    return k


def find_lucky_no(a):
    if len(a) == 1:
        return a

    b = remove_two(a)
    c = remove_three(b)

    return find_lucky_no(c)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print("h+++++++++++++++++++++++")
print(find_lucky_no(a))

# i = 0

# len_a = len(a)
# k = []

# while i < len(a):
#     k.append(a[i])
#     i += 2
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# b = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# c = [1, 3, 7, 9, 13, 15, 19]
#
# while i < len(a):
#     if (i+1) % 2 != 0:
#         k.append(a[i])
#     i += 1
#

# while i < len(b):
#     if (i+1) % 3 != 0:
#         k.append(b[i])
#     i += 1

# print(k)


