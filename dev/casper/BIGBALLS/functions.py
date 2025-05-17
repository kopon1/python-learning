import csv
import datetime


inventory = {}


def load_inventory(filename):
    # Reads inventory.csv and returns a dictionary {ball_type: quantity}
    with open("csv_files/inventory.csv", "r") as csv_file:
        fieldnames = ["Ball Type", "Quantity"]
        csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames)
        for line in csv_reader:
            print(line)

def save_inventory(filename, inventory):
    # Writes inventory dictionary back to inventory.csv
    with open("csv_files/inventory.csv", "a") as csv_file:
        fieldnames = ["Ball Type", "Quantity"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writerows(inventory)
    

def record_sale(inventory):
    # Ask user which ball, how many; update inventory and log to sales.csv
    
    pass

def record_purchase(inventory):
    # Ask user which ball, how many; update inventory and log to purchases.csv
    
        pass

def view_inventory(inventory):
    # Print out current stock of all balls
    with open("csv_files/inventory.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            print(line)
    

def monthly_report(year, month):
    # Load sales.csv and show total of each ball_type sold in that month
    pass

def main_menu():
    # Display menu and loop through options until exit
    while True:
        print(f"Big Balls Inc.\n{input_validation("What would you like to do?\nEnter 1 to Record a Sale.\nEnter 2 to Record a Purchase.\nEnter 3 to View Current Inventory.\nEnter 4 to View Monthly Report. ")}")
    
# Validate user input or prompt user to exit the program
def input_validation(question):
    while True:
        try: 
            choice = input(f"{question}\nEnter 'q' to exit.\n")
            if choice == 'q'.lower():
                print("Exiting...")
                break
            elif choice == '1':
                record_sale("sales.csv")
            elif choice == '2':
                record_purchase("purchases.csv")
            elif choice == '3':
                view_inventory("inventory.csv")
            elif choice == '4':
                pass
            elif choice <= '1' or choice >= '4':
                print("Please enter a valid choice between 1-4.")
                return
            else:
                print("Invalid input.")
        except ValueError as e:
            print("Error: ", e)
                    
main_menu()