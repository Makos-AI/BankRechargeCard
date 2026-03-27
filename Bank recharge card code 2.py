acctn_enter = int(input("Enter your account number"))
acct_db = 99
import time

def delayed_timer(message,time):
    print(f"...")
    time.sleep(3)
    print("Process terminated.")

if acctn_enter != acct_db:
    print("Invalid. try again")
    
    while acctn_enter != acct_db:
        print("Invalid. Try again")
        acctn_enter = int(input("Enter account number"))
        
    print("Valid account number") 

        
else:
    print("Valid account number.")
    
print("Next stage loading...")

pin_enter = int(input("Enter your 4 digit pin"))
#Need to add contraint preventing pin from being more than 4 values, and from not being number/
pin_db = 123

if pin_enter != pin_db:             #Pin code
    print("Invalid pin. Try again later")
    while pin_enter != pin_db:          #While loop for pin code. Allows you to put in acct no again, and runs acct no code
        acctn_enter = int(input("Enter your account number"))
        if acctn_enter != acct_db:
            print("Invalid account number")
            while acctn_enter != acct_db:
                print("Invalid. Try again")
                acctn_enter = int(input("Enter your account number"))
            print("Valid account number.")
            
        else:
            print("Valid account number") 
        print("Next stage loading...")   #Acct no code completed. Begins to go to pin code
        
        pin_enter = int(input("Enter your pin"))
        if pin_enter == pin_db:         #Pin code, tests pin. As it is still in the while loop, even if the if or else condition is satisfied,
            print("Correct pin entered.\nStage 2 completed.\nNext stage loading...")  #It does not leave the loop UNLESS the while loop condition is 
                        #nullified, and then it can break out.
        else:
            print("Invalid pin. Try again")
    
else:
    print("Correct pin entered. \nStage 2 completed.\nNext stage loading...")
    
print("Select account to debit: \n1. Savings\n2. Default\n3. Current\n4. Back")
sel_service = int(input("Select: "))
savings_bal = 100000 
default_bal = 10000000
current_bal =10000
if sel_service == 1:
    acct_bal = savings_bal
    print("Savings account selected.\nProceeding to next stage...")
elif sel_service == 2:
    acct_bal = default_bal
    print("Default account selected.\nProceeding to next stage...")
elif sel_service ==3:
    acct_bal = current_bal
    print("Current account selected.\nProceeding to next stage...")
    #NB: For later update of this code, let each of the accounts have their respective restrictions that they would have in a normal bank app
    #Study how these accounts work and incorporate them in code
elif sel_service == 4:
    print("Back option selected.\nTerminating process now...")
    print("...") #After 3 seconds
    print("Process terminated. Thank you for using the Jomi Online banking app")#
    #Need to find out how to end the entire program frm this option
    #If option is 4, then while you deduct for the other accounts, for this one, no other options would be included for the option 4
else:
    print("Invalid answer. Reselect options")
    while sel_service != (1 or 2 or 3 or 4):
        print("Invalid answer. Select a valid option")
        print("Select account to debit:\n1. Savings\n2. Default account\n3. Current\n4. Back")
        sel_service = int(input("Select: ")) #While loop is used to ensure that user only selects one of the options. NB: Using letters still crashes the code
        #Preventive method 1: Use an elif or an else. If using else, turn the else containing the while loop to an elif, by putting the comdition as 
        #sel_service != (1 or 2 or 3 or 4) and is an integer and then use the below code normally. the else would take care of everything else(pun)
        
print("Select credit bundle:\n1. N100\n2. N200\n3. N300\n4. N500\n5. N700\n6. N1000\n7. 1500\n8. N2000\n9. N5000\n10. N10,000\n11. N25,000\n12. N50,000\n13. Back ")
credit_select = int(input("Select: "))
print

credit_bal = 0
bought_balance = 0

def buying_bundle():
    print("N" + str(bought_bundle) + " bundle selected")
    global acct_bal, credit_bal
    if acct_bal >= bought_bundle:
        acct_bal = acct_bal - bought_bundle
        print("Congratulations!You have purchased the N" + str(bought_bundle) + " credit bundle.")
        print("Initial credit balance = " + str(credit_bal))
        credit_bal = credit_bal + bought_bundle
        print("Your account balance is: " + str(acct_bal))
        print("Your credit balance is: " + str(credit_bal))
        
    else:
        print("Insufficient account balance. Please ensure you are using the right account to purchase this bundle.")


if credit_select == 1:
    bought_bundle = 100
    buying_bundle()
        
elif credit_select == 2:
    bought_bundle= 200
    print("N200 bundle selected")
    if acct_bal >= bought_bundle:
        acct_bal = acct_bal - bought_bundle
        print("Congratulations! You have purchased the N200 credit bundle.")
        print("Initial credit balance= " + str(credit_bal))
        credit_bal = credit_bal + bought_bundle
        print("Your account balance is: " + str(acct_bal))
        print("Your credit balance is: " + str(credit_bal))
        
        
    else:
        print("Insufficient account balance. Please ensure you are using the right account to purchase this bundle")
        
elif credit_select == 3:
    bought_bundle = 300
    print("N300 bundle selected.")
    if acct_bal >= bought_bundle:
        acct_bal = acct_bal - bought_bundle
        print("Congratulations! You have purchased the N300 credit bundle.")
        print("Initial credit balance = " + str(credit_bal))
        credit_bal = credit_bal + bought_bundle
        print("Your account balance is: " + str(acct_bal))
        print("Your credit balance is " + str(credit_bal))
        
    else:
        print("Insufficient account balance. Please ensure you are using the right account to purchase this bundle")
        
elif credit_select == 4:
    print("N500 credit bundle selected.")
    bought_bundle = 500
    if acct_bal >= bought_bundle:
        acct_bal = acct_bal - bought_bundle
        print("Congratulations! You have purchased the N500 credit bundle. " )
        print("Initial credit balance = " + str(credit_bal))
        credit_bal = credit_bal + bought_bundle
        print("Your account balance is:  " + str(acct_bal))
        print("Your credit balance is: " + str(credit_bal))
        
    else:
        print("Insufficient account balnce. Please ensure that you are using the right account to purchase this bundle")
        
elif credit_select == 5:
    bought_bundle = 700
    print("N700 bundle selected")
    if acct_bal >= bought_bundle:
        acct_bal = acct_bal - bought_bundle
        print("Congratulations!You have purchased the N700 credit bundle.")
        print("Initial credit balance = " + str(credit_bal))
        credit_bal = credit_bal + bought_bundle
        print("Your account balance is: " + str(acct_bal))
        print("Your credit balance is: " + str(credit_bal))
        
    else:
        print("Insufficient account balance. Please ensure you are using the right account to purchase this bundle.")
        
elif credit_select == 6:
    bought_bundle = 1000
    print("N100 bundle selected")
    if acct_bal >= bought_bundle:
        acct_bal = acct_bal - bought_bundle
        print("Congratulations!You have purchased the N1000 credit bundle.")
        print("Initial credit balance = " + str(credit_bal))
        credit_bal = credit_bal + bought_bundle
        print("Your account balance is: " + str(acct_bal))
        print("Your credit balance is: " + str(credit_bal))
        
    else:
        print("Insufficient account balance. Please ensure you are using the right account to purchase this bundle.")
        
elif credit_select == 7:
    bought_bundle = 1500
    print("N100 bundle selected")
    if acct_bal >= bought_bundle:
        acct_bal = acct_bal - bought_bundle
        print("Congratulations!You have purchased the N1500 credit bundle.")
        print("Initial credit balance = " + str(credit_bal))
        credit_bal = credit_bal + bought_bundle
        print("Your account balance is: " + str(acct_bal))
        print("Your credit balance is: " + str(credit_bal))
        
    else:
        print("Insufficient account balance. Please ensure you are using the right account to purchase this bundle.")
        
elif credit_select == 8:
    bought_bundle = 2000
    print("N2000 bundle selected")
    if acct_bal >= bought_bundle:
        acct_bal = acct_bal - bought_bundle
        print("Congratulations!You have purchased the N2000 credit bundle.")
        print("Initial credit balance = " + str(credit_bal))
        credit_bal = credit_bal + bought_bundle
        print("Your account balance is: " + str(acct_bal))
        print("Your credit balance is: " + str(credit_bal))
        
    else:
        print("Insufficient account balance. Please ensure you are using the right account to purchase this bundle.")
 
 
     
            
elif credit_select == 9:
    bought_bundle = 5000
    buying_bundle()
    
elif credit_select == 10:
    bought_bundle = 10000
    buying_bundle()
    
elif credit_select == 11:
    bought_bundle = 25000
    buying_bundle()  

elif credit_select == 12:
    bought_bundle = 50000
    buying_bundle()
    
elif credit_select == 13:
    print("Process terminating...")
    print("...") #after 3 seconds
    delayed_timer()


  