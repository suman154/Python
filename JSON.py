# # JSON in python 
# import json

# # some json
# x = '{"name":"Rahul", "age":"30", "city":"Kathmandu"}'

# # parse x:
# y = json.loads(x)

# # the result is a python dictionary.
# print(y["name"])
# # print(y["age"])
# # print(y["city"])

# Convert from Python to JSON:
import json

# a python object (dict)
x = {
    "name":"Barsha",
    "age":"29",
    "city":"Lalitpur"
}

# convert into json
y = json.dumps(x)







# * the result is JSON string:
# print(y)
# You can convert Python objects of the following types, into JSON strings:
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None



# # Example
# # Convert Python objects into JSON strings, and print the values:
import json

print(json.dumps({"name": "shyam", "age": 79}))
print(json.dumps(["apple", "Orange"]))
print(json.dumps(("apple", "watermealon")))
print(json.dumps("hello"))
print(json.dumps(77))
print(json.dumps(99.99))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))




# Convert a Python object containing all the legal data types:
import json

x = {
  "name": "Ramesh",
  "age": 27,
  "married": True,
  "divorced": False,
  "children": ("sita","Gita"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 21.5},
    {"model": "Ford Edge", "mpg": 29.1}
  ]
}

print(json.dumps(x))




#* Format the Result
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))



# Example:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))





#* Order the Result
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
