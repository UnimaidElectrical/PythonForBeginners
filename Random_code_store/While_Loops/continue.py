#continue jumps back to the top of the loop rather than stopping
# An example can be shown below

i=0
while True:
    i=i+1
    if i==2:
        print("skipping 2")
        continue
    if i==5:
        break
    print(i)
print("Finished")

'''
The continue statement in Python returns the control to the beginning of the current loop. 
When encountered, the loop starts next iteration without executing the remaining statements in the current iteration.
'''
#The continue statement can be used in both while and for loops.

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

#The while statement loops through the values and when it finds 5 omits it by continueing the loop
var = 10                    # Second Example
while var > 0:              
   var -=1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")
