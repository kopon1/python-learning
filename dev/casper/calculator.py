
from funcs import input_to_int, appropiate_input_num, remove_lines
import csv
import datetime

# Dict that saves user inputs
inputs = {}

# function that gets the current time and formats it
def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%D-%M-%Y, %H:%M")

# function that handles user's choice to add, divide, multiply or substract
def calc():
    while True:
        num1 = appropiate_input_num("Choose your first number ")
        if num1 is None: return
    
        num2 = appropiate_input_num("Choose your second number ")
        if num2 is None: return    
        
        opt = input_to_int("Enter:\n1 to add\n2 to multiply\n3 to divide\n4 to subtract")

# if statements*** change opt variable and convert user input into operator +*/-
        if opt == 1:
            opt = "+"
            result = num1 + num2
        elif opt == 2:
            opt = "*"
            result = num1 * num2                
        elif opt == 3:
            opt = "/"
            result = num1 / num2
            if num2 == 0:
                print("Can't divide by zero")
                continue
            else:
                result = (num1 / num2)   
        elif opt == 4:
            opt = "-"
            result = num1 - num2
        elif opt is None:
            return
        else:
            print("Invalid choice, please try again")
                            
# compress code into printing final result and append to inputs dict
        total = f"{num1} {opt} {num2} = {round(result, 2)}"
        print(total)
        try:
            key = get_current_time()
            if key in inputs:
                inputs[key].append(total)
            else:
                inputs[key] = [total]
            with open("inputs.csv", "a") as csv_file:
                my_dict = {f"{get_current_time()}: {[total]}"}
                # fieldnames = ["Time", "Operations"]
                csv_writer = csv.writer(csv_file, delimiter="\t")
                for line in my_dict:
                    csv_writer.writerow(line)
        except AttributeError:
            pass     
        
# function that prompts user to access calculator or exit 
def user_choice():
    while True:
        try:
            choice = input_to_int("What would you like to do?\nEnter:\n1 to access calculator\n2 to access previous history\n3 to delete history")
            if choice == 1:
                calc()
            elif choice == 2:
                with open("inputs.csv", "r") as csv_file:
                    fieldnames = ["Time", "Operations"]
                    csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames, delimiter="\t")
                    for line in csv_reader:
                        print(line)
            elif choice == 3:
                delete_input()
            elif choice is None:
                return
            else:
                print("Please enter a valid choice.")
        except Exception as e:
            print("Error", e)

# function that handles deleting user inputs from file 
def delete_input():
    while True:
# open file and read it, then print it to the user enumerating the lines
        f = open("inputs.csv", "r")
        for x, element in enumerate(f):
                print(f"{x}: {element}")       
        opt = input_to_int("This is your saved history.\nEnter which number you want to delete from history.")
        if opt is None:
            return
        remove_lines("inputs.csv", [opt])
        
user_choice()
print(inputs)


    









