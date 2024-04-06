
account_number=input("Enter account number: ")
if ((len(account_number) == 4) and (account_number[0]==1)):
    account_number = int(account_number)
    
    account_balance=int(input("Enter your balance: "))
    if (account_balance>=100000):
        salary=int(input("Enter your Salary: "))
        loan_type=input("Enter loan type: ")
        loan_amount_expected=int(input("Enter expected loan amount: "))
        customer_emi_expected=int(input("Enter expected EMI: "))  
        if((salary>25000) and (loan_type=='Car')and(loan_amount_expected>=500000)and(customer_emi_expected>=10000)):
            print ("loan approved")
        else:
            print("loan not approved")   
    else:
        print("Your balance is not insuffient for loan.") 
else:
    print("Account number only 4 digit and starts with 1.")

  

  
