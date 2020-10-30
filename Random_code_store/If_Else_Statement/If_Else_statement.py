"""This mimicks the children games where we are asked to choose our own adventure
"""

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input ("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you want to do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")


    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear=="2":
        print("The bear eats your leg off. Good job!")
    else:
        print(f"Well doing,  {bear} is probable better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity =="2":
        print("Your body survives powered by the mind of jello.")
        print("Good Job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good Job!")

else:
    print("You stumble around and fall on a knife and die. Good Job!")










# Else Statements
# break
# continue


# The else statement is most commonly used along with the if statement, but it can also follow a for or while loop, which gives it a different meaning.
# With the for or while loop, the code within it is called if the loop finishes normally (when a break statement does not cause an exit from the loop).

Example:
for i in range(10):
   if i == 999:
      break
else:
   print("Unbroken 1")

for i in range(10):
   if i == 5:
      break
else: 
   print("Unbroken 2")

# The first for loop executes normally, resulting in the printing of "Unbroken 1".
# The second loop exits due to a break, which is why it's else statement is not executed.




# Try
# Except


# The else statement can also be used with try/except statements.
# In this case, the code within it is only executed if no error occurs in the try statement.
# Example:

#Example2:
try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)

try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)


# Example 2:
try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)




