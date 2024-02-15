#Create a variable named carname and assign the value Volvo to it.
carname = "Volvo"

#Create a variable named x and assign the value 50 to it.
x = 50

#Display the sum of 5 + 10, using two variables: x and y.
x = 5
y = 10
print(x+y)

#Create a variable called z, assign x + y to it, and display the result.
x = 5
y = 10
z = x + y
print(z)

#Insert the correct syntax to assign values to multiple variables in one line:
x , y , z = "apple", "mango", "banana"
print(x)
print(y)
print(z)

#Insert the correct syntax to assign the same value to all three variables in one code line.
x = y = z = " I Love Coding"
print(x)
print(y)
print(z)

#Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
    global x 
    x = "fantastic"
    