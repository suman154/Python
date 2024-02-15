#Add List Items
#*Append Items
#Exmpe:
thelist  = ["apple","banana", "mango", "cherry"]
thelist.append("orange")
print(thelist)

#*Insert Items
# Example
# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#*Extend List
# Example
# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)



#*Add Any Iterable
# Example
# Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


