#Linear and Bisection Search (Binary)
#Iterative implementation

def bisection_iter(n, arr):
    start = 0
    stop = len(arr)-1
    while start <= stop:
        mid = (start + stop)//2
        if n == arr[mid]:
            return f"{n} found in the list: {mid}"
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1
    return f"{n} not found in the list"

def create_list(max_val):
    arr = []
    for num in range (1, max_val+1):
        arr.append(num)
    return arr

#l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#ind 0  1  2  3  4  5  6  7  8  9
#num_to_search = 5

l = create_list(10)
for num in range(16):
    print(bisection_iter(num, l))





#Recursive Implementation of bisection search 

def bisection_recur(n, arr, start, stop):
    if start > stop:
        return f"{n} not found in list"
    else:
        mid = (start + stop) // 2
        if n == arr[mid]:
            return f"{n} is found at index: {mid}"
        elif n > arr[mid]:
            return bisection_recur(n, arr, mid + 1, stop)
        else:
            return bisection_recur(n, arr, start, mid - 1)


def create_list(max_val):
    arr = []
    for num in range(i ,max_val +1):
        arr.append(num)
    return arr


#l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#ind 0  1  2  3  4  5  6  7  8  9
for num in range(16):
    print(bisection_recur(num, l, 0, len(l)-1))






