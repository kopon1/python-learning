import datetime as dt
import csv

# List of numbered months used in monthly_report. Int wont return 01-09 and error appears
months_str = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

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
            
def record_sale_invntry(saved_quantity: int, saved_inventory: list, ball_type) -> bool:
    try:
        with open("inventory.csv", "w", newline="") as csv_file:
            fieldnames = ["Ball Type", "Quantity"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=",")
            csv_writer.writeheader()
            updated_inventory = []
            for sale_dict in saved_inventory:
                if sale_dict["Ball Type"] == ball_type:
                    sale_dict["Quantity"] = str(saved_quantity)
                    updated_inventory.append(sale_dict)
                else:
                    print(f"Unexpected error. Please try again.")
                    return
            csv_writer.writerows(updated_inventory)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
        
def date():
    now = dt.datetime.now()
    return now.strftime("%m-%d-%Y")

# Current year for user validation in monthly_report() instead of manually updating it yearly
# This func might be used for future user options
def year_now():
    now = dt.datetime.now()
    year = int(now.strftime("%Y"))
    return year
