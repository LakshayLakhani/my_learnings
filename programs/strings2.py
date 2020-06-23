# Given strings, find the leftmost character that repeats.

string = "lakshay"
res = 10000
fi = [-1 for i in range(256)]

for i in range(len(string)):
    if fi[ord(string[i])] == -1:
        fi[ord(string[i])] = i
    else:
        res = min(res, fi[ord(string[i])])

if res == 10000:
    print(-1)
else:
    print(res)





