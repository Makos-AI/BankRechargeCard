import time

# Simulated database values
acct_db = 99
pin_db = 123
savings_bal = 100000
default_bal = 10000000
current_bal = 10000
credit_bal = 0

# Function to simulate a delay
def delayed_timer(message, delay):
    print("Exiting system...")
    time.sleep(delay)
    print(message)

# Function to handle account number entry
def enter_account_number():
    while True:
        acctn_enter = (input("Enter your account number: "))
        
        if acctn_enter.isdigit():
            
            if int(acctn_enter) == acct_db:
                print("Valid account number.")
                return
            else:
                print("Invalid account number. Try again.")

# Function to handle PIN entry
def enter_pin():
    
    while True:
        pin_enter = int(input("Enter your 4-digit PIN: "))
        if pin_enter == pin_db:
            print("Correct PIN entered. \nStage 2 completed.\nNext stage loading...")
            return
            break
        else:
            
            print("Invalid PIN. Try again.")
            enter_account_number()
            
            while True:
                pin_enter = int(input("Enter your 4-digit PIN"))
                if pin_enter == pin_db:
                    print("Valid PIN")
                    break
                else:
                    while pin_enter != pin_db:
                        print("Invalid PIN. Try again la")
                        enter_account_number()
                        pin_enter = int(input("Enter your 4-digit PIN"))
                        if pin_enter == pin_db:
                            break
                        else:
                            print()
                    break
            break
    
                
            

# Function to select account to debit
def select_account():
    global savings_bal, default_bal, current_bal
    while True:
        print("Select account to debit:\n1. Savings\n2. Default\n3. Current\n4. Back")
        sel_service = int(input("Select: "))
        if sel_service == 1:
            print("Savings account selected.\nProceeding to next stage...")
            return savings_bal
        elif sel_service == 2:
            print("Default account selected.\nProceeding to next stage...")
            return default_bal
        elif sel_service == 3:
            print("Current account selected.\nProceeding to next stage...")
            return current_bal
        elif sel_service == 4:
            print("Back option selected.\nReturning to previous menu...")
            return "back"
        else:
            print("Invalid option. Please select a valid account.")

# Function to handle bundle purchase
def select_credit_bundle(acct_bal):
    global credit_bal
    while True:
        print(
            "Select credit bundle:\n1. N100\n2. N200\n3. N300\n4. N500\n5. N700\n6. N1000\n7. N1500\n"
            "8. N2000\n9. N5000\n10. N10,000\n11. N25,000\n12. N50,000\n13. Back"
        )
        credit_select = int(input("Select: "))
        if credit_select == 13:  # Back option
            print("Returning to previous menu...")
            return "back"
        
        bundle_values = {
            1: 100, 2: 200, 3: 300, 4: 500, 5: 700,
            6: 1000, 7: 1500, 8: 2000, 9: 5000,
            10: 10000, 11: 25000, 12: 50000
        }

        if credit_select in bundle_values:
            bought_bundle = bundle_values[credit_select]
            if acct_bal >= bought_bundle:
                acct_bal -= bought_bundle
                credit_bal += bought_bundle
                print(f"Congratulations! You have purchased the N{bought_bundle} credit bundle.")
                print(f"Remaining account balance: N{acct_bal}")
                print(f"Updated credit balance: N{credit_bal}")
                break
            else:
                print("Insufficient account balance. Please try again.")
        else:
            print("Invalid selection. Please try again.")
            

# Main flow of the program
def main():
    print("Welcome to Jomi Online Banking!")
    while True:
        enter_account_number()
        enter_pin()
        
        # Account selection
        while True:
            acct_bal = select_account()
            if acct_bal == "back":
                break  # Go back to PIN entry
            else:
                # Bundle selection
                while True:
                    action = select_credit_bundle(acct_bal)
                    if action == "back":
                        break  # Go back to account selection
                    break
            #break
        break
        

    print("Thank you for using Jomi Online Banking!")
    delayed_timer("...", 3)
    print("Program closed.")
    #break

# Run the program
main()