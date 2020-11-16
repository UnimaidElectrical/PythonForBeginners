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


def bisection_iter(n, arr):
    start = 0
    stop = len(arr)-1
    mid = (start + stop)//2
    if n == arr[mid]:
        return f" {n} found at index: {mid}"
    elif n > arr[mid]:
        start = mid + 1
    else:
        return f" {n} not found in list"
    #print(arr[mid])
    #return f"{n} not found in the list"

def create_list(max_val):
    arr = []
    for num in range(1, max_val+1):
        arr.append(num)
    return arr
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_to_search = 8
print(bisection_iter(num_to_search,l))




