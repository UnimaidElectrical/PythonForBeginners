#Quick Sort Implementation
**************************


def quicksort(arr):
    """
    Input: Unsorted list of intergers
    Returns sorted list of integers using Quicksort
    Note: This is not an in-place implementation. The In-place implementation with follow shortly after.
    """

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return smaller + equal + larger
l=[6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print(quicksort(l))


'''
***********************
        return smaller , equal , larger    #For this reason the final list will be returned as a tuple instead of a list.
        #To stop this from happening we then concatenate the 
l=[6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]    
print(type(quicksort(l)))
this will be returned as a tuple.
************************
'''





def quicksort(arr):
    """
    Input: Unsorted list of integers
    Returns sorted list of integers using Quicksort
    Note: This is not an in-place implementation. The In-place implementation with follow shortly after.
    """

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
                #running the quick sort algo on the smaller list will return a sorted list in th
        return smaller + equal + larger
l=[6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print(type(quicksort(l)))




****************************8


def quicksort(arr):
    """
    Input: Unsorted list of integers
    Returns sorted list of integers using Quicksort
    Note: This is not an in-place implementation. The In-place implementation with follow shortly after.
    """

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
                #running the quick sort algo on the smaller list will return a sorted list in th
        return smaller + equal + larger
l=[6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print(type(quicksort(l)))