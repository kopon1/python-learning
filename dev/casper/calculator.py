
from funcs import input_to_int, appropiate_input_num, remove_lines
import csv


# Dict that saves user inputs
inputs = {}

def user_choice():
    while True:
        try:
            choice = input_to_int("What would you like to do?\nEnter:\n1 to access calculator\n2 to access previous history\n3 to delete history")
            if choice == 1:
                calc()
            elif choice == 2:
                with open("inputs.csv", "r") as csv_file:
                    fieldnames = ["Time", "Operations"]
                    csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames)
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
# function that handles user's choice to add, divide, multiply or substract
def calc():
    while True:
        num1 = appropiate_input_num("Choose your first number ")
        if num1 is None: return
    
        num2 = appropiate_input_num("Choose your second number ")
        if num2 is None: return    
        
        opt = input_to_int("Enter:\n1 to add\n2 to multiply\n3 to divide\n4 to subtract")
        
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
                csv_writer = csv.DictWriter(csv_file, fieldnames=None)
                for timestamp in inputs:
                    for operation in inputs[timestamp]:
                        new_row = {
                            "Time": str(timestamp),
                            "Operation": str(operation)
                        }
                        csv_writer.fieldnames = new_row.keys()
                        csv_writer.writerow(new_row)
        except AttributeError:
            pass     
             
user_choice()


if __name__ == "__main__":
    print("RUNNING CALCULATOR")
    user_choice()









