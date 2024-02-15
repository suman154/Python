#*Many Values to Multiple Variables
#Exmple: 
x , y , z = "Physics", "Chemistry", "Math"
# print(f"{x} {y} {z}")
print(x)
print(y)
print(z)

#*One Value to Multiple Variables
x = y = z = "Python"
 # print(f"{x} {y} {z}")
print(x)
print(y)
print(z)

#*Unpack a Collection
language = ["python","Java", "C++",]
x , y, z = language
print(x)
print(y)
print(z)


# #*Output Variables
#Exmple:1
x = "python is awesome"
print(x)

#Exmple:2
x = "python"
y = "is"
z = "awesome"
print(x,y,z)


#Exmple:3
x = "python "
y = "is "
z = "awesome "
print(x + y + z)


#For numbers, the + character works as a mathematical operator:
# x = 899
# y = 601
# print(x+y)


#Error:
# x = 5
# y = "John"
# print(x + y)

#Exmple:4
x = 45
y = 25
print(x,y)



















num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
sum = num1 + num2
# print("The sum of {} and {} is {}".format(num1, num2,
#                                          sum))
print("The sum of {},{} is {}".format(num1, num2, sum))