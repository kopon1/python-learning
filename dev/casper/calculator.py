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
    answer = x / y
    return answer

# function for substracting

def substract(x,y):
    answer = x - y
    return answer


# TEST
num1 = input_to_int("Choose your first number ")
num2 = input_to_int("Choose your second number ")
print(substract(num1, num2))