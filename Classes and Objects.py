# python class and object
#* Create a Class
class Myclass:
    x = 10

print(Myclass)


#* Create Object
class Myclass:
    x = 10

p1 = Myclass()
print(p1.x)


#* The __init__() Function
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("Kumar", 91)

print(p1. name)
print(p1. age)


#* The __str__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person ("Sita", 31)
print(p1)

# Example:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("Rita", 42)

print(p1)


#* Object Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Hari", 25)
p1.myfunc()



#* The self Parameter
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Krishna", 66)
p1.myfunc()


#* Modify Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Rita", 29)

p1.age = 35

print(p1.age)




#* Delete Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

print(p1.age)


#* Delete Objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)





