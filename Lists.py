#*Python Lists
#Exmple:
# Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

#*Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

# Example
# Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


#*List Length
# To determine how many items a list has, use the len() function:

# Example
# Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))



#* List Items - Data Types
# List items can be of any data type:

# Example
# String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list can contain different data types:

# Example
# A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]
print(list1)


#*type()
#xmple:
#What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))



#*The list() Constructor
# Example
# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.