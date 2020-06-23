# given a sorted array count the no. of occurences of an element  .

arr = [2, 3, 3, 3, 3, 5, 5, 7, 8]
count_for = 5
op = 4
low = 0
high = len(arr)
                        #3   #5
                        #2   #5
def binary_search(arr, low, high, count_for):
    mid = (high+low) // 2  #3 #4
    if count_for == arr[mid] and arr[mid ] != count_for or mid == high-1:
        return  mid
    elif count_for >= arr[mid]:
        return binary_search(arr, mid+1, high, count_for)
    else:
        return binary_search(arr, low, mid-1, count_for)

print(binary_search(arr, low, high, count_for))