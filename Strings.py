#Python Strings
#*String
#Exmple:
print("Hello, World!")  #Double Quotes
print('Hello, World!')  #Single Quotes


#*Assign String to a Variable
#Exmple: 
name = "Hello, How are you?"   #Variable name is assigned the value of string 'John Do
#Printing the variable
print(name)

#*Multiline Strings
#Exmple:
paragraph = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""" 
print(paragraph) #three double quotes


paragraph = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(paragraph) #three single quotes


#* String are Arrays
#In Python strings can be treated as arrays and we can access individual characters in them using indexing.
fruit = "apple"
print(fruit[0])    #Output: a (First character of the string)



#*Looping Through a String
#Exmple:
for s in "Sujan":
    print(s)       # Output: S u j a n
    

#*String Length
#Exmple:
    text = "Hello, World!"
    length = len(text)
    print("The length of the text is :",length)

#*Check String
    text = "The best things are in life are free!"
    print("free" in text)

#Use it in an if statement:
    txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


  #*Check if NOT
  text = "The best thing in the life is free!"
  print ("expensive" not in text)

  #Use it in an if statement:
  text = "The best thimmg in the life is free!"
  if "expensive" not in text:
     print("No, 'expensive' is not present")