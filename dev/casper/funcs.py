

# Validate user input into an integer and handle exceptions

def input_to_int(question):
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
      
def remove_lines(filepath, lines_to_remove):
    f = open(filepath, "r+")
    with open("inputs.txt", "r+") as file:
        lines = f.readlines()
        f.seek(0)
        f.writelines(line for i, line in enumerate(lines) if i + 1 not in lines_to_remove)
        f.truncate()



        

        
        
        
        
        
        
        
        
        
    

            