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


# TEST
def choice():
    while True:
        try:
            choice = input_to_int("What would you like to do? Enter 1 to access calculator")
            if choice == 1:
                calc = input_to_int("What would you like to do? 1, for add, 2 for m, 3 for s, 4 div")
                if calc == 1:
                    print(add(num1, num2))
                

            elif choice is None:
                return
            else:
                print("Please enter a valid choice")
        except Exception:
            print("Error")
                        
choice()
print("Hmm, quit? test test test")
    

# num1 = input_to_int("Choose your first number ")
# num2 = input_to_int("Choose your second number ")
# print(divide(num1, num2))