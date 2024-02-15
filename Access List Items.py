#*Access Items
#Exmple:
# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#*Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
# Example:
# Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


#*Range of Indexes
# Example:
# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


#Example:
#This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


#Example
#This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#*Range of Negative Indexes
#The syntax is similar to normal range of indexes, except that it starts
#from the end instead of the beginning.
thislist = ["apple", "banana", "cherry", "orange", " kiwi", "melon", "mango"]           
print(thislist[-3:-1])

#Check if Item Exists
#Example
#Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")