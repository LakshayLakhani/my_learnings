#left rotate an array d way 

l = [10, 20, 30, 40 ,50]

l_output = [20, 30, 40, 50, 10]

n = len(l)

d = 5

for i in range(d):
  first = l[0]
  for i in range(1, n):
    l[i-1] = l[i]
  
  l[-1] = first

print(l)

#method 2 
#left rotate an array d way O(n)

l = [10, 20, 30, 40 ,50]

l_output = [20, 30, 40, 50, 10]

n = len(l)

d = 3

n_a = [i for i in range(d)]

for i in range(d):
  n_a[i] = l[i]

for i in range(d, n):
  l[i-d] = l[i]

for i in range(d):
  l[n-d+i] = n_a[i]

print(l)
    



