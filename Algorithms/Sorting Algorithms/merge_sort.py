#Merge sort

#The implementation of merge sort will be done in small chuncks so a new user can really grasp the full picture

def merge_sorted(arr1,arr2):
    print("Merge function called with lists below:")
    print(f"left: {arr1} and right {arr2}")
    sorted_arr=[]
    i,j=0,0

    if arr1[i] < arr2[j]:
        sorted_arr.append(arr1[i])
        i +=1
    else:
        sorted_arr.append(arr2[j])
        j+=1
    print(f"Left list index i is {i} and has value: {arr1[i]}")
    print(f"Right list index j is {j} and has value: {arr2[j]}")
    return sorted_arr

# xxxxxxxxxxxxxxxx Program Execution xxxxxxxxxxxxxxxx
l1=[2,4,6,8,10]
l2=[1,3,5,7,8,9]
print(f"Un-merged list: {merge_sorted(l1,l2)}")

#Steps:
#1, Compare first element in each list and append smaller elements
#2, Using indices and an interior, perform same comparison for all elements in both lists
#3, Move marker up by 1 position after smaller number is found
#4, copy remaining list once comparisons are complete and there are items still remaining in one of the lists






Part 2



def merge_sorted(arr1,arr2):
    print("Merge function called with lists below:")
    print(f"left: {arr1} and right {arr2}")
    sorted_arr=[]
    i,j=0,0
    while i < len(arr1) and j < len(arr2):
        # print(f"Left list index i is {i} and has value: {arr1[i]}")
        # print(f"Right list index j is {j} and has value: {arr2[j]}")
        # i+=1
        # j+=1
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i +=1
        else:
            sorted_arr.append(arr2[j])
            j+=1
        # print(f"Left list index i is {i} and has value: {arr1[i]}")
        # print(f"Right list index j is {j} and has value: {arr2[j]}")
        print(sorted_arr)
    return sorted_arr

# xxxxxxxxxxxxxxxx Program Execution xxxxxxxxxxxxxxxx
l1=[2,4,6,8,10]
l2=[1,3,5,7,8,9]
print(f"Un-merged list: {merge_sorted(l1,l2)}")


#part 3
#This will catch the cases not covered in the previous steps. The cases where l1 or l2 are empty lists

def merge_sorted(arr1,arr2):
    print("Merge function called with lists below:")
    print(f"left: {arr1} and right {arr2}")
    sorted_arr=[]
    i,j=0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i +=1
        else:
            sorted_arr.append(arr2[j])
            j+=1
    while i<len(arr1):
        sorted_arr.append(arr1[i])
        i+=1
    while j<len(arr2):
        sorted_arr.append(arr2[j])
        j+=1
        print(sorted_arr)
    return sorted_arr

# xxxxxxxxxxxxxxxx Program Execution xxxxxxxxxxxxxxxx
l1=[2,4,6,8,10,11,12,13,14]
l2=[1,3,5,7,8,9,15,16]
print(f"merged list: {merge_sorted(l1,l2)}")



#part 4
def merge_sorted(arr1,arr2):
    #Wrapping these in a function
    print("Merge function called with lists below:")
    print(f"left: {arr1} and right {arr2}")
    sorted_arr=[]
    i,j=0,0

    #seperating the blocks of code that compares and combines two lists
    #here we are checking for the largest of each element in the list this is possible because the list is already sorted.
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i +=1
        else:
            sorted_arr.append(arr2[j])
            j+=1

    #Here we are checking if all the elements of the first list are more than those of the second list
    #The missing exception being that the second list is empty or we have bigger elements at the end of the first list
    while i<len(arr1):
        sorted_arr.append(arr1[i])
        i+=1

    # Here we are checking if all the elements of the Second list are more than those of the first list.
    # This includes cases where the first list is empty
    while j<len(arr2):
        sorted_arr.append(arr2[j])
        j+=1
        print(sorted_arr)
    return sorted_arr

# xxxxxxxxxxxxxxxx Program Execution xxxxxxxxxxxxxxxx
l1=[2,4,6,8,10,11,12,13,14]
l2=[1,3,5,7,8,9,15,16]
print(f"merged list: {merge_sorted(l1,l2)}")






def divide_arr(arr):
    if len(arr) < 2:
        print(f"Base condition reached with {arr[:]}")
        print(f"{arr[:]}")
        return arr[:]
    else:
        middle = len(arr)//2
        print("Current list to work with:", arr)
        print("Left split:", arr[:middle])
        print("Right split: ", arr[middle:])
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
l= [8,6,7,2,5] #[3,7,5,9,1,4,2,8,10] #  [3,7,5,-3,9,1,-4,4,-5,2,8,-2,10,-1]  #
divide_arr(l)
#print(arr)



Complete Merge Sort 



def merge_sorted(arr1,arr2):
    sorted_arr = []
    i,j=0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i+=1
        else:
            sorted_arr.append(arr2[j])
            j+=1
        #print(sorted_arr)
    while i < len(arr1):
            sorted_arr.append(arr1[i])
            i+=1
    while j < len(arr2):
            sorted_arr.append(arr2[j])
            j+=1
    print(sorted_arr)
    return sorted_arr

def divide_arr(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        return merge_sorted(l1,l2)
l =[3,7,5,-3,9,1,-4,4,-5,2,8,-2,10,-1]
    #[2,3,6,8,10]
#l2 = [1,3,5,7,8,9]
print(divide_arr(l))