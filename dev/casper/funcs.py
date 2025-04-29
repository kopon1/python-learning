

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
            
def appropiate_input_num(question, number_type=None):
    while True:
        input_to_int(question)
        if number_type is None:
                if '.' in number_type:
                    try:
                        return float(number_type)
                    except ValueError:
                        pass
                else:
                    try:
                        return int(number_type)
                    except ValueError:
                        pass
        else:
            try:
                if number_type == int:
                    return int(number_type)
                elif number_type == float:
                    return float(number_type)
                elif number_type == complex:
                    return complex(number_type)
                else:
                    raise ValueError("Invalid number type specified.")
            except ValueError:
                pass
        print("Please enter a valid input.")
            
        
            