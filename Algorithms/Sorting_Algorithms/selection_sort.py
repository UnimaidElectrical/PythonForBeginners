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





Insertion sort explained.


we need a marker which will move through the list on the outer loop
Start iteration and compasins at first element 


Then check if the number on the second element smaller than the number at the marker. If not we can move to the next element.
Next we check the third element with the marker if it is smaller than the marker (First Element) then do a swap else move to the next element on the list.
We keep checking the next element with the marker until the end of the list.

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)



















































def bubble_sort(arr):
    sort_head = True
    while sort_head:
        print("Bubble Sort: " + str(arr))
        sort_head = False
        for num in range(len(arr)-1):
            if arr[num]>arr[num+1]:
                sort_head = True
                arr[num],arr[num+1]=arr[num+1],arr[num]

l = [4,1,6,4,8,10,28,-3,-45]
bubble_sort(l)



def selection_sort(arr):
    spot_marker=0
    while spot_marker < len(arr):
        for num in range(spot_marker,len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[spot_marker],arr[num]=arr[num],arr[spot_marker]
                #print('Item Swapped')
        spot_marker += 1
        print(arr)

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort(l)









def selection_sort(arr):
    spot_marker = 0
    while spot_marker < len(arr):
        for num in range(spot_marker,len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[spot_marker],arr[num]=arr[num],arr[spot_marker]
        spot_marker += 1
        print(arr)

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort(l)
