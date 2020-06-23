#O(n^^2) solution .

arr = [2,3,10,6,4,8,1]

n = len(arr)
diff = 0

for i in range(n):
  for j in range(i+1, n):
    if j > i:
      new_diff = arr[j] - arr[i]
      if diff > new_diff :
        diff = diff
      else:
        diff = new_diff

#O()