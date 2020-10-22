#Linear and Bisection Search (Binary)

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





