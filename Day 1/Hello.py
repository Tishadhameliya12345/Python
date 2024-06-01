#Simple python syntax 
print("Hello")

#Type casting
x = str(6)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#Get the Type
print(type(x))

#Case sansitive
a=10
A="Tisha"
print(a)
print(A)

# Assign multiple value
a,b,c="Tisha","Harsh","Jay"
print(a)
print(b)
print(c)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Globle Variable
x = "TD"
def myfunc():
  print("Hi-" + x) # Globle variable
myfunc()

# Use of Globle Keyword
def myfunc():
  global x
  x = "TD"
myfunc()
print("Hi " + x)