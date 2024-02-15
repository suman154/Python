# Python RegEx
#* RegEx Module
import re


#Check if the string starts with "The" and ends with "Spain"
txt = "The rain in spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes! We have a match!")
else:
    print("No Match")






#* The findall() Function
import re

#Return a list containing every occurrence of "ai":
txt = "Please replace all occurrences of 'ai' with 'ay'"
x = re.findall('ai', txt)
print(f"Found '{x}'\n")

# Example:
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)






#* The search() Function
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", 
x.start()) 






#* The split() Function
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)




#* The sub() Function
import re

txt = "The rain in Spain"
x = re.sub('\s', "9", txt)
print(x)



#* Match Object
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())



import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)



import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())