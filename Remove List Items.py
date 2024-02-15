# Remove List Items
#*Remove Specified Item
# ExampleGet your own Python Server
# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)



#*Remove Specified Index
# The pop() method removes the specified index.

# Example
# Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# The del keyword also removes the specified index:

# Example
# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.

# Example
# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist



#*Clear the List
# Example
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)