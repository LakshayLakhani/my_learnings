#recursive way

string = "l"
l = 0
r = len(string)-1

def check_palindrom(l, r, string):

    if string[r] != string[l]:
        return False
    if l < r:
        check_palindrom(l+1, r-1, string)

    return True

print(check_palindrom(l, r, string))
