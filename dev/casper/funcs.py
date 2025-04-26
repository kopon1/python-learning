

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
            