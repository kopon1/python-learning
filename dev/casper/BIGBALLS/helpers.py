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
def reduce_stock():
    with open("inventory.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=None)
        for line in csv_reader:
            print(line)
    



def date():
    now = dt.datetime.now()
    return now.strftime("%m-%d-%Y")

reduce_stock()