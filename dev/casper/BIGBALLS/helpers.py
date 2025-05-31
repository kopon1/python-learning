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
            
            
# def reduce_stock(ball, amnt_sold):
#     while True:
#         with open("csv_files/inventory.csv", "r") as csv_file:
#             csv_reader = csv.DictReader(csv_file, fieldnames=None)
#             # for x, element in enumerate(csv_reader):
#             #     print(f"{x}: {element}")
#             for line in csv_reader:
#                 num = line["quantity"]
#                 my_list = [int(num) - int(amnt_sold)]
#                 if ball == line["ball_type"]:
#                     with open("csv_files/inventory.csv", "w", newline="") as csv_writer:
#                         fieldnames = ["Ball Type", "Quantity"]
#                         csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=",")
                        
#                 elif ball not in line["ball_type"]:
#                     print("HMM")
#                     return
#                 else:
#                     print("Error")
            
            




def date():
    now = dt.datetime.now()
    return now.strftime("%m-%d-%Y")
