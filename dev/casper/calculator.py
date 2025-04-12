from funcs import input_to_int
# Calculator Project


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
            return answer
        except ZeroDivisionError:
            print("Can't divide by zero meat head.")
            return None

# function for substracting

def substract(x,y):
    answer = x - y
    return answer


# function that handles user's choice to add, divide, multiply or substract
def calc():
    opt = input_to_int("Enter:\n1 to add\n2 to multiply\n3 to divide\n4 to substract")
    while True:
        if opt == 1:
            num1 = input_to_int("Choose your first number ")
            num2 = input_to_int("Choose your second number ")
            print(add(num1, num2))
        elif opt == 2:
            num1 = input_to_int("Choose your first number ")
            num2 = input_to_int("Choose your second number ")
            print(multiply(num1, num2))
        elif opt == 3:
            num1 = input_to_int("Choose your first number ")
            num2 = input_to_int("Choose your second number ")
            print(divide(num1, num2))
        elif opt == 4:
            num1 = input_to_int("Choose your first number ")
            num2 = input_to_int("Choose your second number ")
            print(substract(num1, num2))
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
        except Exception:
            print("Error")
                        
print(user_choice())
print("exiting program test test test")
    












# num1 = input_to_int("Choose your first number ")
# num2 = input_to_int("Choose your second number ")
# print(divide(num1, num2))