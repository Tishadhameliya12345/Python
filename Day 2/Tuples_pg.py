# Tuples in Python
#Tuples are used to store multiple item in single variable

#Create a Tuple
#Tuples contain diffrent datatype
# it start from '()'
Tuple_1=("apple",True,"Cherry",156,'A',"Banana",345,False)
print(Tuple_1)

#Find a lenght throw len() function
print(len(Tuple_1))

print(type(Tuple_1))

#Access item from Tuple
print(Tuple_1[1])
print(Tuple_1[-1]) #Nagativ Index

#Range of Indexes
print(Tuple_1[2:4])
print(Tuple_1[-4:-1])

#Check if item in Tuple or not
if "apple" in Tuple_1:
    print("Yes, Apple in List")
else:
    print("Apple is not in List")
    
#Change Tuple item(cannot converted)
#Convert the tuple into a list to be able to change it:
a=("Tisha","Jay","Jensi") # Tuple
b=list(a) # change in list
b[2]="Harsh" # change value
a=tuple(b) # list convert in tuple
print(a)

#insert item in Tuple
#Append item in Tuple
# (index_value, Value)
# also for remove()

c=("Tisha","Jay","Jensi") # Tuple
d=list(c) # change in list
d.append("Harsh") # add value
d.remove("Jensi") # remove item
c=tuple(d) # list convert in tuple
print(c)

# Unpaking TUple
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits # Use of Asterisk*

print(green)
print(yellow)
print(red)

#Extend two List
List_2=("Jay",1234,'J')
Tuple_1.extend(List_2)
print(Tuple_1)


# Using a Loop

#For loop
Tuple1=("Tisha",123456,"T","Harsh",24457644,"H",True)
for i in Tuple1:
    print(i)
    
# While loop
while i<=len(Tuple1):
    print(Tuple1[1])
    i=i+1

# Join two Tuple using '+'
Tuple2=("Jensi","Dev",123,"A")
Tuple3 = Tuple1 + Tuple2
print(Tuple3)

# multiply Tuple
Tuple4 = Tuple2 * 2
print(Tuple4)