#Insertion sort

'''
this is typically done in ascending order

def insertion_sort(arr):
    key = 0
    sorting = True
    while sorting:
        sorting = False
        for num in range(key,len(arr)):
            if arr[key] > arr[num]:
                arr[key], arr[num]=arr[num],arr[key]
                sorting = True
        key +=1
        print(arr)

lists = [3,7,5,-3,9,1,-4,4,-5,2,8,-2,10,-1] #[3,7,5,9,1,4,2,8,10] #
insertion_sort(lists)
'''




#2,
'''
def insertionSort(my_list):
    ## for every element in our array
    for index in range(1, len(my_list)):
        current = my_list[index]
        position = index

        while position > 0 and my_list[position-1] > current:
            print("Swapped {} for {}".format(my_list[position], my_list[position-1]))
            my_list[position] = my_list[position-1]
            print(my_list)
            position -= 1

        my_list[position] = current

    return my_list

my_list = [3,7,5,-3,9,1,-4,4,-5,2,8,-2,10,-1]

print(insertionSort(my_list))
'''






#Implementing in a different way
'''
def insertion_sort(arr):
    for key in range(1,len(arr)):
        print("first for loop with fresh keys: "+ str(key) +' and: '+ str(len(arr)))
        if arr[key] < arr[key-1]:
            print("if statement locatn (arr[key]): "+str(arr[key]) + ' and previous location (arr[key-1]): ' + str(arr[key-1]))
            j=key
            while j> 0 and arr[j] < arr[j-1]:
                print("the while loop here, with J as: " +str(j)+ ' and arr[j] as: ' +str(arr[j]) + ' and arr[j-1] as: '+ str(arr[j-1]))
                arr[j],arr[j-1] = arr[j-1],arr[j]
                j-=1
                print ('the increment of j: '+ str(j))
lists = [3,7,5,-3,9,1,-4,4,-5,2,8,-2,10,-1]  #[3,7,5,9,1,4,2,8,10]   #
insertion_sort(lists)
#print(insertion_sort(lists))
print(lists)
'''

def insertion_sort(arr):
    for key in range(1,len(arr)):
        if arr[key] < arr[key-1]:
            j=key
            while j> 0 and arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                j-=1
lists = [3,7,5,-3,9,1,-4,4,-5,2,8,-2,10,-1]  #[3,7,5,9,1,4,2,8,10]   #
insertion_sort(lists)
print(lists)