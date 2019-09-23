# The break statement can be used to prematurely end the while loop
# The break statement can also be used to immediately end a loop.

i=0
while 1==1:  # the code will keep running as far as this remains true 
    print(i)
    i=i+1
    if i > 5:
        print("Breaking")
        break
print("Finished")


# using the break statement outside a llop can cause an error  