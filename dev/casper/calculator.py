
from funcs import input_to_int, appropiate_input_num, remove_lines
import csv
import datetime

# List that saves user inputs
inputs = []
f = "inputs.csv"
headers = []

# function that gets the current time and formats it
def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%D-%M-%Y, %H:%M:%S")

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
                
# compress code into printing final result and append to inputs list
            total = f"{num1} {opt} {num2} = " f"{round(result, 2)}"
            inputs.append(f"{total}, {get_current_time()}")
            print(total)
            
# append inputs list to file
            with open("inputs.csv", "a") as csv_file:
                fieldnames = ["Operations", "Time"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter="\t")
                csv_writer.writeheader()
            
                for line in inputs:
                    csv_writer.writerow(line + "\n")
                    
           
            
            
# function that prompts user to access calculator or exit 
def user_choice():
    while True:
        try:
            choice = input_to_int("What would you like to do?\nEnter:\n1 to access calculator\n2 to access previous history\n3 to delete history")
            if choice == 1:
                calc()
            elif choice == 2:
                with open("inputs.csv", "r") as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter="\t")
                    
                    for line in csv_reader:
                        print(line)
            
                # f = open("inputs.csv", "r")
                # for x, line in enumerate(f):
                #     print(f"{x}: {line}")
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



    









