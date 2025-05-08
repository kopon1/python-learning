
from funcs import input_to_int, appropiate_input_num, remove_lines
import csv
import datetime as dt

# Inputs needs to be created only once, so it is global to the whole program
# I will write to it while the program is going and only add the contents to the CSV in the when it shuts down
# Inputs should be created from the CSV if it exists, but lets leave that for later
inputs = { }

# This probably belongs on funcs.py since its useful for other projects.
def get_current_datetime_without_seconds():
    return dt.datetime.now().strftime("%D-%M-%Y, %H:%M")
    
# function that handles user's choice to add, divide, multiply or substract
def calc():
    while True:
            num1 = appropiate_input_num("Choose your first number ")
            if num1 is None: return
        
            num2 = appropiate_input_num("Choose your second number ")
            if num2 is None: return    
            
            opt = input_to_int("Enter:\n1 to add\n2 to multiply\n3 to divide\n4 to subtract")

            # Calculate result
            # result = 0
            if opt == 1:
                opt = "+"
                result = num1 + num2
            elif opt == 2:
                opt = "*"
                result = num1 * num2 
            elif opt == 3:
                opt = "/"
                if num2 == 0:
                    print("Can't divide by zero")
                    continue
                else:
                    result = num1 / num2
            elif opt == 4:
                opt = "-"
                result = num1 - num2
            elif opt is None:
                return
            else: 
                print("Invalid choice, please try again")
                continue
                
            total = f"{num1} {opt} {num2} = " f"{round(result, 2)}"
            print(total)
            
            # Add operation string to inputs dict
            key = get_current_datetime_without_seconds()
            if key in inputs:
                inputs[key].append(total)
            else:
                inputs[key] = [total]

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

def user_choice():
    while True:
        try:
            choice = input_to_int("What would you like to do?\nEnter:\n1 to access calculator\n2 to access previous history\n3 to delete history")
            if choice == 1:
                calc()
            elif choice == 2:
                # with open("./dev/casper/inputs.csv", "r") as csv_file:
                #     fieldnames = ["Time", "Operations"]
                #     csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames, delimiter="\t")
                #     next(csv_file)
                #     for line in csv_reader:
                #         print(line)
                for k in inputs.keys():
                    print(f"--- {k} ---")
                    for v in inputs[k]:
                        print(f"-> {v}")
            elif choice == 3:
                delete_input()
            elif choice is None:
                return
            else:
                print("Please enter a valid choice.")
        except Exception as e:
            print("Error", e)


if __name__ == "__main__":
    print("RUNNING CALCULATOR")
    user_choice()


    









