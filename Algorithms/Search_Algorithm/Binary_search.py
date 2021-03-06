#Linear and Bisection Search (Binary)
#Sequential Search is a method of looking at each item till you find the item you're looking for. 
# You will eventually get to your desired record in linear time. this gives you a complexity of O(n) or linear search since you're looking through most records.
#log2(12) =3.6
#step count: 4
#To use the Bisection sort, you have to work off a sorted list

'''
def bisection_iter(n,arr):
    return f"{n} not found in the list"

def create_list(max_val):
    arr = []
    for num in range (1, max_val+1):
        arr.append(num)
    return arr
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#ind 0  1  2  3  4  5  6  7  8  9

num_to_search = 5
print(bisection_iter(num_to_search, l))
'''

#Iterative Solution
def bisection_iter(n, arr):
    start = 0
    stop = len(arr)-1
    while start <= stop:
        mid = (start + stop)//2
        if n == arr[mid]:
            return f" {n} found at index: {mid}"
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1
    #print("start = ", start)
    #print("stop = ", stop)
    return f" {n} not found in list"

    #print(arr[mid])
    #return f"{n} not found in the list"

def create_list(max_val):
    arr = []
    for num in range(1, max_val+1):
        arr.append(num)
    return arr
#l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#num_to_search = 1

l = create_list(130)
for num in range(160):
    print(bisection_iter(num,l))




#Recursive Solution

def bisection_recur(n, arr, start, stop):
    if start > stop:
        return f"{n} not found in the list"
    else:
        mid = (start + stop)//2
        if n == arr[mid]:
            return f"{n} found at index: {mid}"
        elif n > arr[mid]:
            return bisection_recur(n, arr, mid+1, stop)
        else:
            return bisection_recur(n, arr, start, mid-1)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in range(16):
    print(bisection_recur(num, l, 0, len(l)-1))