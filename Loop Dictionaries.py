# Loop Dictionaries
#*Loop Through a Dictionary
# Example
# Print all key names in the dictionary, one by one:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

# Example
# You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)

# Example
# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)

#   Example
# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)