# lambda
# Syntax
# lambda arguments : expression
#* Add 100 to argument a, and return the result:
x = lambda a : a + 100
print(x(5))


#* Multiply argument a with argument b and return the result:
y = lambda a, b : a * b 
print(y(5,6))



#* Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(100, 50, 25))


#* Why Use Lambda Functions?
def myfunc(x):
    return lambda a : a * x

mydoubler = myfunc(2)
print(mydoubler(5))


# Exmple:
def my_function(n):
    return lambda a : a * n


mytripler = my_function(3)

print(mytripler(5))


# Exmple:
def my_function(m):
    return lambda a : a * m

mydoubler = my_function(2)
mytripler = my_function(3)

print(mydoubler(10))
print(mytripler(10))