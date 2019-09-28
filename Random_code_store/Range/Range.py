##Range
#The range function creates a sequential list of numbers. usually starts from the least to the max
numbers=list(range(10))
print(numbers)
#The call to list is necessary because range by itself will create a range object. 
# This will be needed to be converted to a list for it to be used later.

nums=list(range(5))
print(nums[4])

# this is alot different because the normal way of counting is len(nums) with a total of 5 items (0,1,2,3,4,5)
nums[0]=0
nums[1]=1
nums[2]=2
nums[3]=3
nums[4]=4


