import datetime

# Validate user input into an integer and handle exceptions
def input_to_int(question: str) -> int:
    while True:
        try:
            num = input(f"{question}\nEnter 'q' to exit.\n")
            if num == "q":
                return None
            elif num:
                return int(num)
            else:
                print("Please enter a valid input.")
        except ValueError as e:
            print("Invalid input.", e)
        except ZeroDivisionError as e:
            print("Can't divide by zero.", e)
        except Exception as e:
            print("Error.", e)

# Validate user input into a float or int and handle exceptions    
def appropiate_input_num(question):
    while True:
        try:
            num = input(f"{question}\nEnter 'q' to exit.\n")
            if num == "q":
                return None
            elif num:
                if '.' in num:
                    return float(num)
                else:
                    return int(num)
            else:
                print("Please enter a valid input.")
        except ValueError as e:
            print("Invalid input.", e)

# remove saved user inputs from file     
def remove_lines(filepath: str, lines_to_remove: int) -> None:
    f = open(filepath, "r+")
    with open("inputs.csv", "r+") as file:
        lines = f.readlines()
        f.seek(0)
        f.writelines(line for i, line in enumerate(lines) if i + 1 not in lines_to_remove)
        f.truncate()

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%D-%m-%Y, %H:%M")

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
        
        
if __name__ == "__main__":
    print("RUNNING CALCULATOR")