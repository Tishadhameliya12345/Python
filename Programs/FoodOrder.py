print("WELCOME TO FOOD CORNER")

print("Which type food you want to??")
print("Please type V for Vegetable and N for non-vegetable:")

food_type=input("V or N: ")

if(food_type=='V'):
    print("It's Vegetable Food")
    qun=int(input("Enter quntity you want: "))
    if(qun>=1):
        print("you price is:")
    else:
        print("Quntity number mininum 1 required.")
elif(food_type=='N'):
    print("It's Non-vegetable Food")
else:
    print("Pleace enter valid Input...!!!!!")
