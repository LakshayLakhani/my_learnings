#normal factorial
# no = 5
#
# def normal_factorial(no):
#     if no == 0 :
#         return 1
#     return no * normal_factorial(no-1)
#
# print(normal_factorial(5))

#tail recursive way

# no = 5
#
# def tail_factorial(no):
#     sol = (no * no-1)
#     return tail_factorial(sol, no-1)
#
# tail_factorial(5)