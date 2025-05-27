# from functions import input_to_int, record_sale, record_purchase, view_inventory, load_inventory, save_inventory, monthly_report, month_year
# import functions
from functions import *
import helpers

def main_menu():
    # Display menu and loop through options until exit
    while True:
        choice = helpers.input_to_int("Big Balls Inc.\nWhat would you like to do?\nEnter 1 to Record a Sale.\nEnter 2 to Record a Purchase.\nEnter 3 to View Current Inventory.\nEnter 4 to View Monthly Report.")
        try: 
            # Needs options for Current Stock report and Monthly Sales report
            if choice is None:
                print("Exiting...")
                return
            elif choice == 1:
                record_sale()
            elif choice == 2:
                record_purchase()
            elif choice == 3:
                view_inventory()
            elif choice == 4:
                pass
            else:
                print("Please enter a valid choice between 1-4.")
        except ValueError as e:
            print("Error: ", e)


if __name__ == '__main__':
    # The following lines get the current directory where Python is running this file.It helps the program know where to look since you might run this on different computers.
    # It also helps if you want to change the folder name or location, you only have to change there reference here
    csv_folder = Path(__file__).parent / "csv_files"
    
    saved_inventory = load_csv(csv_folder / "inventory.csv")
    saved_sales = load_csv(csv_folder / "sales.csv")
    saved_purchases = load_csv(csv_folder / "purchases.csv")
    
    save_csv(csv_folder / "test_sales.csv", saved_sales)

    main_menu()
