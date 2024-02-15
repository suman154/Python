# Python Dates
import datetime

x = datetime.datetime.now()
print(x)

# Example:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))





#* Creating Date object
import datetime

x = datetime.datetime(2024, 1, 29)

print(x)


#* The strftime() Method
import datetime

x = datetime.datetime(2024, 1, 29)


print(x.strftime("%A"))
print(x.strftime("%w"))
print(x.strftime("%d"))
print(x.strftime("%G"))

