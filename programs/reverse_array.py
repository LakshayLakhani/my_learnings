l = [10, 5, 7, 30]

n = len(l)
low = 0
high = n-1

while low<high:
  temp = l[low]
  l[low] = l[high]
  l[high] = temp
  low += 1
  high -= 1

print(l)

#time_complexity = O(n)
#space_compexity = O(1)

