#Python Booleans
#*Boolean Values
#Example:
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Exmple:
# Example
# Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



#Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
# Example
# Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))


# Example
# Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


#*Most Values are True
#Exmple:
#The following will return True:
print(bool([1, 2, 3]))         
print(bool({"name": "John"}))
# print(bool(True))
# print(bool(False))               
# print(bool(None))


# But these will return False:
print(bool([]))
print(bool(0))
print(bool(""))


#* Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
# Example
# The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# Example:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# Functions can Return a Boolean
# You can create functions that returns a Boolean Value:
# Example:
# Print the answer of a function:
def myFunction() :
  return True

print(myFunction())


# Example
# Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


  #Example
# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))

