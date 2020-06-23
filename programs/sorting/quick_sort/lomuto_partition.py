''' Python3 implementation QuickSort using Lomuto's partition
Scheme.'''

''' This function takes last element as pivot, places 
the pivot element at its correct position in sorted 
	array, and places all smaller (smaller than pivot) 
to left of pivot and all greater elements to right 
of pivot '''


def partition(arr, low, high):
    # pivot
    pivot = arr[high]

    # Index of smaller element
    i = (low - 1)
    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if (arr[j] <= pivot):
            # increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


''' The main function that implements QuickSort 
arr --> Array to be sorted, 
low --> Starting index, 
high --> Ending index '''


# def quickSort(arr, low, high):
#     if (low < high):
#         ''' pi is partitioning index, arr[p] is now
#         at right place '''
#         pi = partition(arr, low, high)
#
#         # Separately sort elements before
#         # partition and after partition
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)


''' Function to pran array '''


# def printArray(arr, size):
#     for i in range(size):
#         print(arr[i], end=" ")
#     print()


# Driver code

# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print("Sorted array:")
# printArray(arr, n)

# This code is contributed by SHUBHAMSINGH10


# My Code .

# arr = [10, 7, 8, 9, 1, 5]
# arr = [0,1,1,0,0,1,1,1,0]
# arr = [2,5,8,7,9,4,3]

arr = [-1, -2 , 4, -3, 4, 9, 7]
n = len(arr)

# j = 0, 1, 2, 3, 4, 5, 6
#i = 0, 1, 2, 3, 4, 4, 5
#arr =[-1, -2,  4, -3, 4 , 7, 9, -8  ]
def partition(arr, low, high): #j = 0, 1, 2, 3, 4, 5, 6, 7
    # pivot                    #i = 0, 1, 1, 2, 2, 2, 2, 3
                               #arr =[-1, -2, -3, 4, ]
    # pivot = arr[high-1] #7
    pivot = 0
    i = (low - 1)

    for j in range(low, high+1):
        # If current element is smaller than or
        # equal to pivot
        if (arr[j] <= pivot):
        # if (arr[j] % 2 == 0):
            # increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high-1] = arr[high-1], arr[i + 1]
    # return (i + 1)
    return arr

print("hello +++++++++++++++++++++++++++++")
print(partition(arr, 0, n-1))


