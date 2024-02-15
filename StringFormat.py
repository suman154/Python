#Python - Format - Strings
#*String Format
#Exmple:
# age = 36
# txt = "My name is John, I am " + age
# print(txt)


#Exmple:
#Use the format() method to insert numbers into strings:
age = 25
weight = 180
height = 70
print("Age: {}, Weight: {}, Height: {}".format(age, weight, height))


#Exmple:
age = 57
txt = "My name is John, and I am {}"
print(txt.format(age))


#Exmple:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))



#Exmple:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
                                               
