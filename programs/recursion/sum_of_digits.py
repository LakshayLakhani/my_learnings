def sum_of_digits(n):
    if n == 0:
        return 0
    b = n % 10
    a = n // 10
    return b + sum_of_digits(a)

print(sum_of_digits(123456))
