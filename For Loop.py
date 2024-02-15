# For Loop
#Exmple
fruits = ["apple", "banana", "mango0"]
for x in fruits:
    print(x)


#* Looping Through a String
    for x in "apple":
        print(x)


#*The break Statement
        fruits = ["apple", "banana", "mango","cherry"]
        for x in fruits:
            print(x)
            if x == "mango":
                break


#*The continue Statement
# Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#*The range() Function
#   Using the range() function:

for x in range(6):
  print(x)

#   Example
# Using the start parameter:

for x in range(2, 6):
  print(x)

# Example
# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)


#*Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")


#Exmple
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


# Nested Loops
#   Example
# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)



    # The pass Statement
    #Exmple
    for x in [0,1,2]:
       pass


