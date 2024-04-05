# An ATM containes indian currence of 100,500,1000. 
# TO withdraw cash from this ATM, the user has to enter no 0 notes he/she wants of each currency ie., 100, 500 and 1000.
# Write a program to calculate the total amount with drawn by the person from the ATM.

amount=int(input("Enter amount you want to: "))

thousand_notes=amount//1000
amount-=thousand_notes*1000

five_hundred_notes=amount//500
amount-=five_hundred_notes*500

hundred_notes=amount//100

print("Thousand_notes: ",thousand_notes)
print("Five HUndred Notes: ",five_hundred_notes)
print("Hundred: ",hundred_notes)