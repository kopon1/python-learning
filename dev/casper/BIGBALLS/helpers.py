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
            
def record_sale_invntry(saved_quantity: int, saved_inventory: list) -> bool:
    try:
        with open("../inventory.csv", "w", newline="") as csv_file:
            fieldnames = ["Ball Type", "Quantity"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=",")
            csv_writer.writeheader()
            updated_inventory = []
            for sale_dict in saved_inventory:
                sale_dict["Quantity"] = str(saved_quantity)
                updated_inventory.append(sale_dict)
            csv_writer.writerows(updated_inventory)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
            
def date():
    now = dt.datetime.now()
    return now.strftime("%m-%d-%Y")
