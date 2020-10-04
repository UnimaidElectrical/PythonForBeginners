# Bubble Sort
# Bubble sort steps through the list and compares adjacent pairs of elements. 
# The elements are swapped if they are in the wrong order. 
# The pass through the unsorted portion of the list is repeated until the list is sorted. 
# Because Bubble sort repeatedly passes through the unsorted part of the list, it has a worst case complexity of O(n²)


def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                    
    return arr

arr = [3,2,10,19,-1]
bubble_sort(arr)
print(arr)