# Python Numbers
# There are three numeric types in Python:

# int
# float
# complex

#Exmple:
x = 5  #int
y = 5.8  #float
z = 6j  #complex

print(type(x))
print(type(y))
print(type(z))



#* Integer (Int)
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#exmple:
x = 9
y = 45789942
z = -3478001

print(type(x))
print(type(y))
print(type(z))




#* Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

# Example:
a = 5.8
b = 3.14e2   #This means 3.14 *
c = .000001
d = 9/4      # This is also a float because the division result is not an
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Example:
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))



#*Complex
# Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))



#* Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:
#Exmple:

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))



#Random Number
import random
random_number = random.randint(0,9) #generate an integer between
print("The Random number is :",random_number)