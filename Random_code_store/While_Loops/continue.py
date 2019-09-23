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