import os 
import csv 
from functionind import verify_user, calculate_tax, save_to_csv, read_from_csv, total_tax_relief

def mainind():

    print("Welcome to Malaysia Tax Input Program")
    #define the CSV file where the data will be stored 
    csv_filename = os.path.abspath(r"C:\Users\Fion\python program\individual asm\msia_tax_data.csv")

    #confirm full file path for debugging
    print(f"[DEBUG] Tax data will be saved to : {os.path.abspath(csv_filename)}")

    #check if user registered 
    registered_users = read_from_csv (csv_filename)

    #check if user is registered, else prompt to registration 
    user_found = False 
    while not user_found:
        ic_number = input("Enter your 12 digit IC number: ")
        password = input("Enter the last 4 digit of your IC number as password: ")

        if registered_users is None or ic_number not in registered_users['ID'].values:
            print("New user. Please register.")
            if verify_user(ic_number, password):
                print("Registration successfully")
                registered_users = read_from_csv(csv_filename)
                user_found = True
            else:
                print("Invalid IC number and password. Please try again.")
        else:
            if verify_user(ic_number, password):
                print("Login successful")
                user_found = True
            else:
                print("Invalid password. Please try again")
 

    # After successfully login, proceed to tax calculation
    try:
        income = float(input("Enter your annual income (in RM):"))
        tax_relief = total_tax_relief()
    except ValueError:
        print("Please enter valid number for income and tax relief")
        return 

    #calculate tax payable 
    tax_payable = calculate_tax(income, tax_relief)
    print (f"Your tax payable is: RM {tax_payable:.2f}")

    #store user data in CSV file 
    data_to_save = [ic_number, password, income, tax_relief, tax_payable]
    print(f"[DEBUG] Saving this data : {data_to_save}")
    save_to_csv(data_to_save, csv_filename)

    #display all tax records
    show_record = input("Would you like to view all tax record? (yes/no):").lower()
    if show_record == "yes":
        tax_record = read_from_csv(csv_filename)
        print(tax_record)
    else:
        print("Thank you!")
if __name__ == "__main__":
    mainind()






