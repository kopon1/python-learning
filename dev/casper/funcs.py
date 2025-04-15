

# Validate user input into an integer

def input_to_int(question):
    while True:
        try:
            num = input(f"{question}\nEnter 'q' to exit.\n")
            if num == "q":
                return None
            elif num:
                return float(num)
            else:
                print("Please enter a valid input.")
        except ValueError as e:
            print("Invalid input.", e)
        except ZeroDivisionError as e:
            print("Can't divide by zero.", e)
        except Exception as e:
            print("Error.", e)
            
            
# Save user input, operator and return value 


# def collect_process_inputs():
    
#     # List where valid user inputs will be saved
#     inputs = [
        
#     ]
#     for i in range(4):
#         save_inputs = input_to_int(question="")
#         inputs.append(save_inputs)
        
#     result = " | ".join(inputs)
    
#     return inputs, result