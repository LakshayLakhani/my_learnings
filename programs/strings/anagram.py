
def is_anagram(string1, string2):
    count1 = [0 for i in range(256)]
    count2 = [0 for i in range(256)]

    for i in range(len(string1)):
        count1[ord(string1[i])] += 1

    for i in range(len(string2)):
        count2[ord(string2[i])] += 1

    for i in range(256):
        if count1[i] != count2[i]:
            return False

    return True

string1 = "lakshay"
string2 = "lakhani"

# print(is_anagram(string1, string2))
