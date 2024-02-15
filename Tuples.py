# Tuples
# Example
# Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Example
# Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#*Tuple Length
# Example
# Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#*Create Tuple With One Item
# Example
# One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#*The tuple() Constructor
# Example
# Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

