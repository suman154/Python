# Python Scope
#* Local Scope
def my_function():
    x = 500
    print(x)

my_function()



#* Function Inside function
def my_function():
    x = 48500
    def myinnerfunction():
        print(x)
    myinnerfunction()

my_function()




#* global Scope
x = 5800
def my_functiona():
    print(x)

my_functiona()
print(x)




#* Namling Variables
x = 7900
def my_function():
    x = 5700
    print(x)

my_function()
print()


#* Global Keyboard
def my_function():
    global x 
    x = 4500

my_function()
print(x)

# Example:
x = 5800
def my_function():
    global x 
    x = 8900

my_function()
print(x)




