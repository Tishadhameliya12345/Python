# Creating a class in Python
class MyClass:
    x="Me"

# Creat object of class
c1 = MyClass()
print(c1.x)

#Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tisha", 20)

print(p1)

# Using __str__() Function object return value of object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("Tisha", 20)

print(p1)

# Method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Tisha", 20)
p1.myfunc()

#
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my age is " + self.age)

p1 = Person("Tisha", 20)
p1.age = 40 # Modify object
p1.myfunc()

'''
1. delete object propertis
    del p1.age 
2. Delete Object
    del p1
'''

