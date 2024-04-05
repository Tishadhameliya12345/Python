# write a program to display take input from the user student name , student subject, marks.

name=input("Enter your Name: ")
sub=input("Enter subject: ")
mak=input("Enter Marks: ")

print('name: ',name)
print('Subject: ',sub)
print('Marks: ',mak)

print(f'name: {name}')

print('name: {0} Subject: {1} Marks: {2}'.format(name,sub,mak))

print(name, sub, mak)