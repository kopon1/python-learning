from funcs import input_to_int
from funcs import appropiate_input_num

# List that saves user inputs
inputs = []

# append user inputs to a file
f = open("inputs.txt")
f.close()

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
                
# compress code into printing final result and append to inputs.txt file
            total = f"{num1} {opt} {num2} = " f"{round(result, 2)}"
            f = open("inputs.txt", "a")
            f.write(total + "\n")
            f.close()
            print(total)

            
# function that prompts user to access calculator or exit 

def user_choice():
    while True:
        try:
            choice = input_to_int("What would you like to do? Enter 1 to access calculator or 2 to access previous history.")
            if choice == 1:
                calc()
            elif choice == 2:
            
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
        f = open("inputs.txt", "r")
        for x, element in enumerate(f):
                print(f"{x}: {element}")
                
        opt = input_to_int("This is your saved history.\nEnter which number you want to delete from history.")
        if opt is None:
            return
        # ***LEN NOT WORKING, FIX IT***
        if opt <= 0 or opt >= len(f):
            print("Pick a number from the list dummy")
            continue
        del f[opt]
        print(f.read())
        f.close()
        return 
        
user_choice()



    









