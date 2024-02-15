#* Creating function
def my_function():
    print("Hello, World!")

# calling function 
my_function()



#* Arguments
def my_function(fname):
    print(fname + " Bhatta ")

my_function("Rahul")
my_function("Shyam")
my_function("Kartik")



#* Number of Arguments
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Ram", "Adhikari")



#* Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("sita", "rita", "gita")


#* Keyboard Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="sita", child2="gita", child3="rita")



#* Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname =  "Gaurav", lname = "Sharma")



#* Default Parameter Value
def my_function(country = "Nepal"):
    print("I am from " + country)


my_function("India")
my_function("Pakistan")
my_function()
my_function("China")




#* Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["Apple", "Banana", "Orange"]

my_function(fruits)



#* Returns Values
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(6))
print(my_function(5))


#* The pass Statement
def my_function():
    pass


#* Positional- Only Arguments
def my_function(x, /):
    print(x)

my_function(10)

# eg:
def my_function(x):
    print(x)

my_function(x=25)




#* Keyword-Only Arguments
def my_function(*, x):
    print(x)

my_function(x=32)

# eg:
def my_function(x):
    print(x)

my_function(5)




#* Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(4, 5, c = 9, d = 3)




#* Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
