#To buy recharge card using simpe code, online bank transaction and the following functions:
#Process of buying recharge capwords(s, sep=None)
#enter account Number
#cross reference database, and if account number is equal to number in database / array, 
# return name of account that corresponds with number (Possibly by cross referencing position or...
#Print list of options of account type (Numbered one to 3), and use if statement along with print input command
# to request for your selection and create a corresponding response
#Next, use print input to request for pin
#cross reference inputed pin value stored in variable with pin value in database (variable, list, array or value)
#If pin variable = pin value in database, proceed to next step
#Select amount you want to pay (ie the bundle you want to pay for)
#Your account is a variable with a value i it. When you select the bundle you want to pay for with print input and
#if, then a print input comes up, asking you for your pin, and pin function is run
#NB: Use Loading... and /n for the period between successive pages / intervals
#After pin function is run, let the variable account balance be reduced by the cost of the package selected
# Let the value of variable credit balace be increased by the amount of credit purchased


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
        sel_service = int(input("Select: "))


    
   # print("N100 bundle selected")
    #if acct_bal >= bought_bundle:
     #   acct_bal = acct_bal - bought_bundle
      #  print("Congratulations!You have purchased the N100 credit bundle.")
       # print("Initial credit balance = " + str(credit_bal))
        #credit_bal = credit_bal + bought_bundle
        #print("Your account balance is: " + str(acct_bal))
        #print("Your credit balance is: " + str(credit_bal))
        
    #else:
    #    print("Insufficient account balance. Please ensure you are using the right account to purchase this bundle.")
        
        
print("Select credit bundle:\n1. N100\n2. N200\n3. N300\n4. N500\n5. N700\n6. N1000\n7. 1500\n8. N2000\n9. N5000\n10. N10,000\n11. N25,000\n12. N50,000\n13. Back ")
credit_select = int(input("Select: "))      
  
  
    
credit_bal = 0
bought_bundle = 0
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