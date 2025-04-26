from funcs import input_to_int

# List that saves user inputs
inputs = []


# function that handles user's choice to add, divide, multiply or substract
def calc():
    
    
    while True:
            num1 = float(input_to_int("Choose your first number "))
            if num1 is None: return
        
            num2 = float(input_to_int("Choose your second number "))
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
                    result = num1 / num2  
                     
            elif opt == 4:
                opt = "-"
                result = num1 - num2

            elif opt is None:
                return
            else:
                print("Invalid choice, please try again")
                
# compress code into printing final result and append to inputs list            
            total = f"{num1} {opt} {num2} = {result}"
            inputs.append(total)
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

def delete_input():
    
    while True:
        for x, element in enumerate(inputs):
                print(f"{x}: {element}")
                
        opt = input_to_int("This is your saved history.\nEnter which number you want to delete from history.")
        if opt is None:
            return
          
        if opt <= 0 or opt >= len(inputs):
            print("Pick a number from the list dummy")
            continue
        del inputs[opt]
        print(inputs)
        return 
        
user_choice()



    









