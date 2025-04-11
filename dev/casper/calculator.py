# Calculator Project


# function for input validation
def input_to_int():
    num = float(input("Choose first number"))
    try:
        num.isdigit()
    except ValueError as e:
        print("Invalid input. Please try again! ", e)
    
    except ZeroDivisionError:
        print("Can't divide by zero, meat head.", e)
        
    except Exception:
        print("Error", e)
validate = input_to_int()

# function for adding
def add(x,y):
    num1 = input()
    num2 = input()
    answer = num1 + num2
    return add(num1, num2)

# function for multiplying

# function for dividing

# function for substracting