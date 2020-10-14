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



6 8 1 4 10 7 8 9 3 2 5

Further explanation
*******************

[6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]


iterating through the list to sort the first time, this will leave us with a n complexity for n element in the array

but because this is being done again and again theoretically, n times for a fully unsorted list, till we get to a sorted list
so in terms of complexity we get n times n or n² in algorithms its called O(n²)

[1,2,3,4,5,6,7,8,8,9,10]

Doing brute force method 

def bubble_sort(arr):
    for num in range(len(arr)-1):      #Because we don't neet to sort for the last element in the list
          print( arr[num]>arr[num+1])   #This sorts the list comparing two element at a time, it runs through the list once, but it is not performing the swap


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)



Performing the swap in place (That is re-addressing the index of one location to the index of another location)

def bubble_sort(arr):
    for num in range(len(arr)-1):    
        if arr[num]>arr[num+1]:                        #This is the condition that prompts the swap to happen
            print("Swap Happened")
            arr[num],arr[num+1]=arr[num+1],arr[num]   #This is where the swap operarion will be
            print(arr)

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)

'''Result:
Swap Happened
[6, 1, 8, 4, 10, 7, 8, 9, 3, 2, 5]
Swap Happened
[6, 1, 4, 8, 10, 7, 8, 9, 3, 2, 5]
Swap Happened
[6, 1, 4, 8, 7, 10, 8, 9, 3, 2, 5]
Swap Happened
[6, 1, 4, 8, 7, 8, 10, 9, 3, 2, 5]
Swap Happened
[6, 1, 4, 8, 7, 8, 9, 10, 3, 2, 5]
Swap Happened
[6, 1, 4, 8, 7, 8, 9, 3, 10, 2, 5]
Swap Happened
[6, 1, 4, 8, 7, 8, 9, 3, 2, 10, 5]
Swap Happened
[6, 1, 4, 8, 7, 8, 9, 3, 2, 5, 10]
'''


The next implementation will be to do the same sort for the whole list for every element

def bubble_sort(arr):
    for num in range(len(arr)):                 #Using the double for loop to go through every possible value
        for num in range(len(arr)-1):    
            if arr[num]>arr[num+1]:                        
                print("Swap Happened")
                arr[num],arr[num+1]=arr[num+1],arr[num]   
                print(arr)

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)

#Here the brute force was implemented for all the possible values. and we see that it bept sorting even after the sort was fully implemented. We can optimize this further
'''Result:
Swap Happened
[6, 1, 8, 4, 10, 7, 8, 9, 3, 2, 5]
Swap Happened
[6, 1, 4, 8, 10, 7, 8, 9, 3, 2, 5]
Swap Happened
[6, 1, 4, 8, 7, 10, 8, 9, 3, 2, 5]
Swap Happened
[6, 1, 4, 8, 7, 8, 10, 9, 3, 2, 5]
Swap Happened
[6, 1, 4, 8, 7, 8, 9, 10, 3, 2, 5]
Swap Happened
[6, 1, 4, 8, 7, 8, 9, 3, 10, 2, 5]
Swap Happened
[6, 1, 4, 8, 7, 8, 9, 3, 2, 10, 5]
Swap Happened
[6, 1, 4, 8, 7, 8, 9, 3, 2, 5, 10]
Swap Happened
[1, 6, 4, 8, 7, 8, 9, 3, 2, 5, 10]
Swap Happened
[1, 4, 6, 8, 7, 8, 9, 3, 2, 5, 10]
Swap Happened
[1, 4, 6, 7, 8, 8, 9, 3, 2, 5, 10]
Swap Happened
[1, 4, 6, 7, 8, 8, 3, 9, 2, 5, 10]
Swap Happened
[1, 4, 6, 7, 8, 8, 3, 2, 9, 5, 10]
Swap Happened
[1, 4, 6, 7, 8, 8, 3, 2, 5, 9, 10]
Swap Happened
[1, 4, 6, 7, 8, 3, 8, 2, 5, 9, 10]
Swap Happened
[1, 4, 6, 7, 8, 3, 2, 8, 5, 9, 10]
Swap Happened
[1, 4, 6, 7, 8, 3, 2, 5, 8, 9, 10]
Swap Happened
[1, 4, 6, 7, 3, 8, 2, 5, 8, 9, 10]
Swap Happened
[1, 4, 6, 7, 3, 2, 8, 5, 8, 9, 10]
Swap Happened
[1, 4, 6, 7, 3, 2, 5, 8, 8, 9, 10]
Swap Happened
[1, 4, 6, 3, 7, 2, 5, 8, 8, 9, 10]
Swap Happened
[1, 4, 6, 3, 2, 7, 5, 8, 8, 9, 10]
Swap Happened
[1, 4, 6, 3, 2, 5, 7, 8, 8, 9, 10]
Swap Happened
[1, 4, 3, 6, 2, 5, 7, 8, 8, 9, 10]
Swap Happened
[1, 4, 3, 2, 6, 5, 7, 8, 8, 9, 10]
Swap Happened
[1, 4, 3, 2, 5, 6, 7, 8, 8, 9, 10]
Swap Happened
[1, 3, 4, 2, 5, 6, 7, 8, 8, 9, 10]
Swap Happened
[1, 3, 2, 4, 5, 6, 7, 8, 8, 9, 10]
Swap Happened
[1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
'''




#Optimizing the solution further, we need to set flags

def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        print("Bubble Status " + str(arr))
        swap_happened=False
        for num in range(len(arr)-1):    
            if arr[num]>arr[num+1]:                        
                swap_happened = True
                arr[num],arr[num+1]=arr[num+1],arr[num]   
        #print(arr)

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)

'''Result:
Bubble Status[6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
Bubble Status[6, 1, 4, 8, 7, 8, 9, 3, 2, 5, 10]
Bubble Status[1, 4, 6, 7, 8, 8, 3, 2, 5, 9, 10]
Bubble Status[1, 4, 6, 7, 8, 3, 2, 5, 8, 9, 10]
Bubble Status[1, 4, 6, 7, 3, 2, 5, 8, 8, 9, 10]
Bubble Status[1, 4, 6, 3, 2, 5, 7, 8, 8, 9, 10]
Bubble Status[1, 4, 3, 2, 5, 6, 7, 8, 8, 9, 10]
Bubble Status[1, 3, 2, 4, 5, 6, 7, 8, 8, 9, 10]
Bubble Status[1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
'''