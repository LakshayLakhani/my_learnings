#left rotate an array 1 way 

# l = [10, 20, 30, 40 ,50]

# l_output = [20, 30, 40, 50, 10]

# n = len(l)

# first = l[0]

# for i in range(n-1):
#   l[i] = l[i+1]

# l[-1] = first

# print(l)

#left rotate an array 2 way 

l = [10, 20, 30, 40, 50]

l_output = [20, 30, 40, 50 ,10]

n = len(l)
first = l[0]
for i in range(1, n):
  l[i-1] = l[i]

l[-1] = first

print(l)










    

