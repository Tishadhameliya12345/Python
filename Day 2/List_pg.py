# List in Python
#List are used to store multiple item in single variable

#Create a list
#List contain diffrent datatype
List_1=["apple",True,"Cherry",156,'A',"Banana",345,False]
print(List_1)

#Find a lenght throw len() function
print(len(List_1))

print(type(List_1))

#Access item from List
print(List_1[1])
print(List_1[-1]) #Nagativ Index

#Range of Indexes
print(List_1[2:4])
print(List_1[-4:-1])

#Check if item in list or not
if "apple" in List_1:
    print("Yes, Apple in List")
else:
    print("Apple is not in List")
    
#Change List item
List_1[3]="Tisha"
print(List_1)

#insert item in List
List_1.insert(8,"Harsh") # (index_value, Value)
print(List_1)

#Append item in List
List_1.append(14560)
print(List_1)

#Extend two List
List_2=["Jay",1234,'J']
List_1.extend(List_2)
print(List_1)

#Find 'e' in apple string 
print(List_1[0][-1])

#Remove List from List
List_1.remove("Tisha")
print(List_1)
