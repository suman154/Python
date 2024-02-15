#Python - Modify Strings
#*Upper Case
#Exmple:
#The upper() method returns the string in upper case:

a = "Hello, Students!"
print(a.upper())
#Output: HELLO, STUDENTS!

print("Hello World".upper())  
# Output: HELLO WORLD



#*Lower Case
#Example:
#The lower() method converts all characters of a string to lowercase.
b = "HELLO, STUDENTS!"
print(b.lower())   
#Output: hello, students!

print("HELLO, STUDENTS!". lower())
# Output: hello, students!


#*Remove Whitespace
#Example:
#The strip() method without any argument removes leading and trailing whitespaces
a = "Hello, Guys!"
print(a.strip()) 
#Output: Hello, Guys!


#*Replace String
#Exmple:
#The replace() method replace a string with another string:
b = "Hello, Vai!"
print(b.replace("V", "D"))

#*Split String
#Exmple:
#The split() method split the spring into substring if it finds intances of the separator:
c = "I love Python programming"
d = c.split()               #default is space
print(d)                     #['I', 'love', 'Python', 'programming']

