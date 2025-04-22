from funcs import input_to_int
# from funcs import collect_process_inputs
# Calculator Project


# List that saves user inputs
inputs = []
# function for adding
def add(x, y):
        answer = x + y
        return answer
# function for multiplying

def multiply(x,y):
    answer = x * y
    return answer

# function for dividing

def divide(x,y):
    while True:
        try:
            answer = x / y
            return round(answer, 2)
        except ZeroDivisionError:
            print("Can't divide by zero meat head.")
            return None

# function for substracting
def substract(x,y):
    answer = x - y
    return answer


# function that handles user's choice to add, divide, multiply or substract
def calc():
    
    
    while True:
            num1 = input_to_int("Choose your first number ")
            if num1 is None: return
        
            num2 = input_to_int("Choose your second number ")
            if num2 is None: return    
            
            opt = input_to_int("Enter:\n1 to add\n2 to multiply\n3 to divide\n4 to subtract")

    # if statements*** change opt variable and convert user input into operator +*/-
            
            if opt == 1:
                opt = "+"
                result = add(num1, num2)

            elif opt == 2:
                opt = "*"
                result = multiply(num1, num2)
                
            elif opt == 3:
                opt = "/"
                result = divide(num1, num2)
                
            elif opt == 4:
                opt = "-"
                result = substract(num1, num2)

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
                        
# print(user_choice())
# print("exiting program test test test")

def delete_input():
    
    while True:
        for x, element in enumerate(inputs, start=1):
                print(f"{x}: {element}")
                
        opt = int(input_to_int("This is your saved history.\nEnter which number you want to delete from history."))
    
        if opt is None:
            return
    
        inp_list = list(inputs)
            
        if opt <= 0 or opt >= len(inp_list):
            print("Pick a number from the list dummy")
            continue
        del inputs[inp_list[opt]]
        return
        


    # List where valid user inputs will be saved

print(user_choice())
print("exiting program test test test")
print(inputs)


    












# num1 = input_to_int("Choose your first number ")
# num2 = input_to_int("Choose your second number ")
# print(divide(num1, num2))