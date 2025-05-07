import pandas as pd
import os 
import csv 

# to verify user 
def verify_user(ic_number, password):
    """Verify the user's IC number and password."""
    if len(ic_number) == 12 and ic_number.isdigit():
        if password == ic_number[-4:]:
            return True 
        else:
            return False 
    return False 

# to calculate tax 
def calculate_tax(income,tax_relief):
    """Calculate tax payable based on income and tax relief."""
    taxable_income = income - tax_relief 
    if taxable_income <= 50000:
        return taxable_income * 0.01 
    elif taxable_income <= 100000:
        return taxable_income * 0.05
    elif taxable_income <= 150000:
        return taxable_income * 0.1 
    else:
        return taxable_income * 0.15
    
# to save user's data into csv file 
def save_to_csv(data, filename):
    """save data to a CSV file."""
    file_exists = os.path.isfile(filename)
    with open(filename, mode= 'a', newline= '') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ID", "password using IC number", "Income(RM)", "Tax Relief(RM)", "Tax payable (RM)"])
        writer.writerow(data)
    
# to read data from CSV 
def read_from_csv(filename):
    """Read data from a CSV file and return it as pandas Dataframe"""
    if os.path.exists(filename):
        return pd.read_csv(filename)
    return None 

def total_tax_relief():
    """Calculate total tax relief"""
    tax_relief = 0 

    #Individual relief 
    tax_relief += 9000

    #spouse relief
    spouse_relief = input("Do you have a spouse with income less than RM4000 per year? (yes/no): ").strip().lower()
    if spouse_relief == "yes":
        tax_relief += 4000

    #child relief
    child_relief = input("How many children do you have? (max 12): ").strip()
    if child_relief.isdigit():
        num_child = min(int(child_relief),12)
        tax_relief += num_child * 8000
    else:
        print("Invalid input for number of children. It will assumed as 0")

    #medical expenses 
    medical_relief = input("Enter your medical expenses for serious medical treatment (max RM 8000: )").strip()
    if medical_relief.replace('.', '', 1).isdigit():
        medical = float(medical_relief)
        tax_relief += min(medical, 8000)
    else:
        print("Invalid input for medical expenses. No relief added")

    #lifestyle spending 
    lifestyle_relief = input("Enter your lifestyle spending (reading materials, sports equipment, computer, smartphone, and internet subscription): ").strip()
    if lifestyle_relief.replace('.', '', 1).isdigit():
        lifestyle = float(lifestyle_relief)
        tax_relief += min(lifestyle, 2500)
    else: 
        print("Invalid input for lifestyle. No relief added.")

    #Education fees 
    education_relief = input("Enter your education course fees (max RM7000):").strip()
    if education_relief.replace('.', '', 1).isdigit():
        education = float(education_relief)
        tax_relief += min(education, 7000)
    else:
        print("Invalid input for education. No relief added.")
    
    #parental care
    parental_relief = input("Enter amount spent on parental care (max RM5000): ").strip()
    if parental_relief.replace('.', '', 1).isdigit():
        parental = float(parental_relief)
        tax_relief += min(parental, 5000)
    else: 
        print("Invalid input for parental care. No relief added. ")

    return tax_relief
