#* Python Arrays
# Example:
cars = ["Ford", "Land Crusior", "BMW"]
print(cars)



#* What is an Array?
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"



#* Access the Elements of an Array
cars = ["Ford", "Land Crusior", "BMW"]
cars[0] = "Creta"
print(cars)


#* The Length of an Array
cars = ["Ford", "Volvo", "BMW"]

x = len(cars)

print(x)



#* Looping Array Elements
cars = ["Ford", "TATA", "BMW"]
for x in cars:
    print(x)



#* Adding Array Elements
cars = ["Ford", "TATA", "BMW"]

cars.append("Creta")

print(cars)



#* Removing Array Elements
cars = ["Ford", "TATA", "BMW"]

cars.pop(1)

print(cars)

#* remove
cars = ["Ford", "Creta", "BMW"]

cars.remove("Creta")

print(cars)
