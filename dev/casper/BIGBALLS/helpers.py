import datetime as dt
import csv


def input_to_int(question: str) -> int:
    while True:
        try:
            ball_type = input(f"{question}\nEnter 'q' to exit.\n")
            if ball_type == "q":
                return None
            elif ball_type:
                return int(ball_type)
            else:
                print("Please enter a valid input.")
        except ValueError as e:
            print("Invalid input.", e)
        except ZeroDivisionError as e:
            print("Can't divide by zero.", e)
        except Exception as e:
            print("Error.", e)
            
            
# def update_csv_quantity(filename, list):
#     with open(filename, "r", newline="") as csv_file:
#         fieldnames = ["Ball Type", "Date", "Quantity"]
#         csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames, delimiter=",")
#         for rows in list:
#             if rows == 
            
            




def date():
    now = dt.datetime.now()
    return now.strftime("%m-%d-%Y")
