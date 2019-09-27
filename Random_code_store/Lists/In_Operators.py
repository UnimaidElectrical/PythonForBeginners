#The In operator in python can be used to determine weather or not a string is a substring of another string.
#what is the optcome of these code:

nums=[10,9,8,7,6,5]
nums[0]=nums[1]-5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])


#To check if an item is not in the list you can use the NOT operator
#In this case the pattern doesn't matter.
nums=[1,2,3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)
