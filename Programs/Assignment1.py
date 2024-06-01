# To read the marks of 5 subjects through the keyboard. Find out the aggrerate and percentage of marks obtained by the student.(max marks 100).

sub1=int(input("Enter Subject 1 Marks: "))
sub2=int(input("Enter Subject 2 Marks: "))
sub3=int(input("Enter Subject 3 Marks: "))
sub4=int(input("Enter Subject 4 Marks: "))
sub5=int(input("Enter Subject 5 Marks: "))

print('total: ',sub1+sub2+sub3+sub4+sub5)

per=(sub1+sub2+sub3+sub4+sub5)/5

print('Persontage is: ',per)

if(per>85):
    print("First class with Distriction.")
elif(per>70 and per<85):
    print("First Class.")
elif(per>50 and per<70):
    print("Pass.")
else:
    print("Fail.")