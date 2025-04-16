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
    opt = input_to_int("Enter:\n1 to add\n2 to multiply\n3 to divide\n4 to subtract")
        
    while True:
        num1 = input_to_int("Choose your first number ")
        if num1 is None: return
        num2 = input_to_int("Choose your second number ")
        if num2 is None: return
        
        if opt == 1:
            result = add(num1, num2)
            inputs.append(...)
            
            print(result)
            return
        elif opt == 2:
            print(multiply(num1, num2))
            return
        elif opt == 3:
            print(divide(num1, num2))
            return
        elif opt == 4:
            print(substract(num1, num2))
            return
        elif opt is None:
            return
        else:
            print("Invalid choice, please try again")
            return
            
            
# function that prompts user to access calculator or exit 

def user_choice():
    while True:
        try:
            choice = input_to_int("What would you like to do? Enter 1 to access calculator")
            if choice == 1:
                calc()
            elif choice is None:
                return
            else:
                print("Please enter a valid choice.")
        except Exception as e:
            print("Error", e)
                        
# print(user_choice())
# print("exiting program test test test")



def collect_process_inputs(inputs, prompt):
    
    # List where valid user inputs will be saved

    for i in inputs:
        
        save_input = user_choice()
        inputs.append(save_input)
    
        result = "|".join(inputs)

        return inputs, result

print(collect_process_inputs(inputs, user_choice()))
print("exiting program test test test")
print(inputs)


    












# num1 = input_to_int("Choose your first number ")
# num2 = input_to_int("Choose your second number ")
# print(divide(num1, num2))