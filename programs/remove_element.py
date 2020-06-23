l = [3,8,12,5,6]

x = 12
n = len(l)

l_O = [3,8,5,6, '']

for i in range(len(l)):
  if l[i] == 12:
    break;

# if i == n:
#   return n

print(i)

for i in range(2, n-1):
  l[i] = l[i+1]

print(l)
