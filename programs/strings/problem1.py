#Given a text string and pattern string, find if a permutation of pattern exists in the text.
from anagram import is_anagram

# string1 = "lakshay"
# string2 = "lakhani"
#
#
#
# print(is_anagram(string1, string2))

ip = "lakshay"
pattern = "lakshay"

for i in range(len(ip)-len(pattern)+1):
    if is_anagram(ip[i:i+len(pattern)], pattern):
        print("yes")
        break





