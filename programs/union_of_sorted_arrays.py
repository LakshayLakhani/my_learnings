a = [3,8,8]
b = [2,8,8,10,15]

i,j =0,0
m,n = len(a), len(b)

while i<m && j<n:
  if i > 0  and a[i] == a[i-1] :
    i += 1
    continue;
  if j > 0 and b[j] == b[j-1]:
    j += 1
    continue;

  if a[i] < b[j]:
    print(a[i])
    i += 1
  elif b[j] < a[i]:
    print(b[j])
    j += 1
  else:
    print(a[i])
    i += 1

while i < m:
  if i == 0 or a[i] != a[i-1]:
    i +=1

while j < n:
  if j == 0 or b[j] != b[j-1]:
    b += 1



Cc: Zhaohui Ning; Debraj Bhattacharya; Roy Chen; Saumya Ranjan Das; Abinash Sarangi; Yue Qi; Ashutosh Singh A; Manoj Kumar MJ; Mayank Jain B; Sergio Agüero; Nikhil Vallabhaneni; Rishabh Mehra; Chevron Gong; Tarun Kumar L; Kuiming Li; Diana Wang H; Anchal Sharma; Nabendu Bikash Roy; Syama Padhy; Debanjan Das; Chandrayee Kumar


    