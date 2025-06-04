import csv
import helpers
from pathlib import Path

# Reads a CSV file and returns a list of dictionaries. Each dictionary represents a row, having the column headers (fieldnames) as keys and the cell values as values
def load_csv(filename: str) -> list:
    while True:
        with open(filename, "r+") as csv_file:
            csv_reader = csv.DictReader(csv_file, fieldnames=None) 
            contents_list = []
            for line in csv_reader:
                contents_list.append(line)
            return contents_list
    
# Takes a list of dictionaries (in the format described in load_inventory) and writes to a CSV file.
# Returns True or False depending on if the writing operation succeeded or not.
# ATTENTION: This should only happen once, when the program is shutdown.
def save_csv(filename: str, rows_list: list) -> bool:
    while True:
        if not rows_list:  # If the list is empty, nothing to write
            return False
        with open(filename, "w", newline="") as csv_file:
            # Get fieldnames from the keys of the first dictionary in the list
            # fieldnames = ["Ball Type", "Date", "Quantity"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=None, delimiter=",")
            csv_writer.fieldnames = rows_list.keys()
            csv_writer.writeheader() # Write the header row
            csv_writer.writerows(rows_list)
        return True  # Return True to indicate success


# Takes the name of a ball and a quantity and registers a new sale (a new dictionary) on the sales object (the list read from the CSV).
# This new entry has the ball type, quantity purchased, and timestamp.
# ATTENTION: You can only sell balls that you currently have in stock!
# ATTENTION #2: DO NOT SAVE TO CSV DIRECTLY. Use the lists that were created by reading the CSVs!
def record_sale(saved_sales: list, saved_inventory: list) -> bool:
    while True:
        ball_type = helpers.input_to_int("What type of ball would you like to buy?\nEnter 1 for Basketballs\nEnter 2 for Bouncy Balls\nEnter 3 for Yoga Balls\nEnter 4 for Tennis Balls\nEnter 5 for Golf Balls")
        if ball_type is None:
            return False
        elif ball_type == 1:
            ball_type = "Basketballs"
        elif ball_type == 2:
            ball_type = "Bouncy Balls"
        elif ball_type == 3:
            ball_type = "Yoga Balls"
        elif ball_type == 4:
            ball_type = "Tennis Balls"
        elif ball_type == 5:
            ball_type = "Golf Balls"
        else:
            print("Invalid input")
            return False
        
        amount = helpers.input_to_int(f"Enter how many {ball_type} would you like to buy.")
        if amount is None: 
            return False
        elif amount <= 0:
            return print("Please enter a valid amount.")
        
        confirmation = input(f"You have purchased {amount} {ball_type}.\nDo you confirm?\nEnter 'Y' for Yes or 'N' for No.\n").upper()
        if confirmation == "Y":
            # Insert new line in sales list
            saved_sales.append({"Ball Type": str(ball_type), "Date": str(helpers.date()), "Quantity": int(amount)})
            # Update inventory values
            for sale_dict in saved_inventory:
                if sale_dict["Ball Type"] == ball_type:
                    saved_quantity = int(sale_dict["Quantity"]) - amount 
                    try:
                        if saved_quantity <= 0 or saved_quantity > 250: 
                            print(f"Unable to buy {amount} {ball_type}\nThis is our current stock.")
                            print(f"{ball_type}: {sale_dict["Quantity"]}")
                            return False
                        elif ball_type == sale_dict["Ball Type"]:
                            sale_dict["Quantity"] = str(saved_quantity)
                            helpers.record_sale_invntry(saved_quantity, saved_inventory, ball_type)
                            return True
                    except ValueError as e:
                        print("Error:", e)     
        elif confirmation == "N":
            return False 
        

# Takes in the name of a ball and a quantity and registers a new purchase (a new dictionary) on the purchases object (the list read from the CSV).
# This new entry has the ball type, quantity purchased, and timestamp.
# ATTENTION: You can only have 250 units max of any ball because the Big Balls Inc. warehouse is pretty small. A purchase that exceeds the stock capacity should not be allowed to happen and the user should be informed.
def record_purchase(saved_purchases: list, saved_inventory: list) -> bool:
    while True:
        ball_type = helpers.input_to_int("What type of ball would you like to buy?\nEnter 1 for Basketballs\nEnter 2 for Bouncy Balls\nEnter 3 for Yoga Balls\nEnter 4 for Tennis Balls\nEnter 5 for Golf Balls")
        if ball_type is None:
            return
        elif ball_type == 1:
            ball_type = "Basketballs"
        elif ball_type == 2:
            ball_type = "Bouncy Balls"
        elif ball_type == 3:
            ball_type = "Yoga Balls"
        elif ball_type == 4:
            ball_type = "Tennis Balls"
        elif ball_type == 5:
            ball_type = "Golf Balls"
        else:
            print("Invalid input")
            return
        amount = helpers.input_to_int(f"Enter how many {ball_type} would you like to buy.")
        if amount is None: 
            return False
        elif amount <= 0:
            return print("Please enter a valid amount.")
        confirmation = input(f"You have purchased {amount} {ball_type}.\nDo you confirm?\nEnter 'Y' for Yes or 'N' for No.\n").upper()
        if confirmation == "Y":
            # Insert new line in sales list
            saved_purchases.append({"Ball Type": str(ball_type), "Date": str(helpers.date()), "Quantity": int(amount)})
            # Update inventory values
            for sale_dict in saved_inventory:
                if sale_dict["Ball Type"] == ball_type:
                    saved_quantity = int(sale_dict["Quantity"]) + amount 
                    try:
                        if saved_quantity >= 250: 
                            print(f"Unable to buy {amount} {ball_type}\nThis is our current stock.")
                            print(f"{ball_type}: {sale_dict["Quantity"]}\nPlease keep our stock below 250.")
                            return False
                        elif ball_type == sale_dict["Ball Type"]:
                            sale_dict["Quantity"] = str(saved_quantity)
                            # helpers.record_sale_invntry(saved_quantity, saved_inventory, ball_type)
                            return True
                    except ValueError as e:
                        print("Error:", e)     
        elif confirmation == "N":
            return False 

# Print out current stock of all balls (from the lists).
def view_inventory(saved_inventory: list):
    print("***Big Balls Inc. Current Inventory***")
    for line in saved_inventory:
        print(line)


# Print out the monthly report for the given year-month combo. Ordered by day ascending.
def monthly_report(saved_sales):
    while True:
        print("***Big Balls Inc. monthly report menu***")
        year = helpers.input_to_int("Enter what year would you like a report on.")
        if year < 2015 or year > helpers.year_now():
            print(f"Please enter a year between 2015-{helpers.year_now()}.")
            return False
        else:
            pass
        month = input(f"Enter what month would you like a report on for the year {year}.\nEnter 'q' to exit.\n").lower()
        if month == 'q':
            return False  
        elif month not in helpers.months_str:
            print(f"Please enter a valid month between 01-12.")
            return False
        else:
                try:
                    for sale_dict in saved_sales:
                        if sale_dict["Date"] == f"{year}-{month}":
                            print(sale_dict)
                    # if sale_dict["Date"] != f"{year}={month}":
                    #     print(f"{year}-{month} not found in sales report. This is our current sales.\n{saved_sales}")
                    #     return False
                except ValueError as e:
                    print("Error:", e)
                except Exception as e:
                    print("Error:", e )