

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
        
        
        
        
        
        
        
        
        
        
        
        # num = input(f"{question}\nEnter 'q' to exit.\n")
        # if num is None:
        #     return None
        # elif '.' in num:
        #     return float(num)
        # elif num is int:
        #     return int(num)
        # else:
        #     try:
        #         if num == int:
        #             return int(num)
        #         elif num == float:
        #             return float(num)
        #         elif num == complex:
        #             return complex(num)
        #         else:
        #             raise ValueError("Invalid number type specified.")
        #     except ValueError:
        #         pass
        # print("Please enter a valid input.")

            