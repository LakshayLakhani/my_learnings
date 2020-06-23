arr = "abcdabceabce"
p = "abce"

len_arr = len(arr)
len_p = len(p)

for i in range((len_arr-len_p)+1):
    if arr[i:i+len_p] == p:
        print("i ++++++++++++++++++++++++")
        print(i)

