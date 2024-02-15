# # Python Module
#* Use a module
import mymodule
mymodule.greeting("Rajesh")




#* Variable in Module - mymodule.py bata import garne 
import mymodule
a = mymodule.person1["name"]
# b = mymodule.person1["age"]
# c = mymodule.person1["country"]
print(a)
# print(b)
# print(c)


# Naming a Module 
#* Re-naming a module
import mymodule 

a = mymodule.person1["age"]
print(a)



#* Built-in Modules
import platform

x = platform.system()
print(x)


#* Using the dir() Function
import platform

x = dir(platform)
print(x)


# Import From Module
from mymodule import person1
print(person1["country"])