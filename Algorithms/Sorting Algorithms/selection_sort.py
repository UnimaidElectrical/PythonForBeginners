# Selection Sort
# Selection sort is also quite simple but frequently outperforms bubble sort.
# With Selection sort, we divide our input list / array into two parts: the sublist 
# of items already sorted and the sublist of items remaining to be sorted that make up 
# the rest of the list. 
# We first find the smallest element in the unsorted sublist and 
# place it at the end of the sorted sublist. Thus, we are continuously grabbing the smallest 
# unsorted element and placing it in sorted order in the sorted sublist.
# This process continues iteratively until the list is fully sorted.


def selection_sort(arr):        
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
            
    return arr

arr = [4,1,6,4,8,10,28,-3,-45]
selection_sort(arr)
print(arr)