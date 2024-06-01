# Finding the nnumber of day in a month.
month=int(input("Enter month: "))

if(month<=12):
    
        if(month==2) : 
            year=int(input("Enter year: "))
    
            # Leap year
            if(year%4==0):
                print("Number of days is 29") 
            # not Leap year
            else:
                print("Number of days is 28")

        elif(month in [1,3,5,7,8,10,12]):
            print("Number of days is 31")

        else:
            print("Number of days is 30")
else:
    print("Wrong month")