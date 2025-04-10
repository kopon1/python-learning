# Calculator Project


# function for input validation
def input_to_int():
    num1 = input("Choose first number")
    num2 = input("Choose second number")
    try:
        num1.isdigit() and num2.isdigit()
    except ValueError as e:
        print("Invalid input. Please try again! ", e)
    
    except ZeroDivisionError:
        print("Can't divide by zero, meat head.", e)
        
    except Exception:
        print("Error", e)

# function for adding
def add(x,y):
    answer = x + y
    num1 = input()
    num2 = input()
    return add(num1, num2)

# function for multiplying

# function for dividing

# function for substracting