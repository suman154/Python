# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

#Exmple
a = 33
b = 200
if b > a:
  print("b is greater than a")

#*Elif
#   Exmple
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#*Else
  a = 200
  b = 55
  if b > a:
    print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  #Exmple
  a = 200
  b = 78
  if b > a :
    print("b is greater than a")
  else:
    print("b is greater than a")

#*Short Hand If ... Else
# You can write an "if statement" as a single line of code with the syntax:
#Exmple
# one line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")



# Example
# One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#*And
a = 4500
b = 457
c = 78
if a > b and c > a:
  print("both condition are true")


#*Or
  a = 199
  b = 66
  if a < 100 or b < 100:
    print("one of the number is less than 100")


#*Not
    a = 45
    b = 84
if not a > b :
    print("a is not greater than b")

#*Nested If
    x = 25
    if x > 10:
      print("Above ten,")
      if x > 20:
        print("amd also above 20!")
else:
 print("but below 20.")

#*The pass Statement
 a = 33
b = 200

if b > a:
  pass