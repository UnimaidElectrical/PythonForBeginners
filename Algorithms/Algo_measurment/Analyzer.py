import time
import random
from Demo import quicksort,mergesort,bubblesort

def create_random_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list
        #print(random.randint(1, 10))
        #print(ran_list)

def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)     #Calls object as one of the parameters #take note!
    tok = time.time()
    seconds = tok-tic
    print(f" {func_name.__name__.capitalize()}\t -> Elapsed time: {seconds:.5f} ")  # the feature after the seconds means that it is being rounded up to 5 decimal places
'''
The dunder function (__name__) gives the name of the function while discarding the extra information
Next we do a function chaining with the capitalize function and then give some tab space inbetween'''

size = int(input("what size list do you want to create? : "))
max_val = int(input("What is the max value of the range? : "))
run_times = int(input("How many times do you want to run? "))
#print(type(size), type(max))
#print(create_random_list(size,max_val))


for num in range(run_times):
    print(f"Run: {num+1}")
    l = create_random_list(size,max_val)
    analyze_func(quicksort,l.copy())
    analyze_func(mergesort,l.copy())
    analyze_func(bubblesort,l.copy())
    analyze_func(sorted,l.copy())   #  this is the inbuilt sorting that is heavily optimized by python.
    print("-" * 40)

'''
#
tic = time.time()
#print(tic)
quicksort(l)
tok = time.time()
#print(tok)
print("QS Elapsed time ->", tok-tic)

tic = time.time()
mergesort(l)
tok = time.time()
print("MS Elapsed time ->", tok-tic)
'''
