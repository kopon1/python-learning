from functions import input_to_int, record_sale, record_purchase, view_inventory, load_inventory, save_inventory, monthly_report, month_year





def main_menu():
    # Display menu and loop through options until exit
    while True:
        choice = input_to_int("Big Balls Inc.\nWhat would you like to do?\nEnter 1 to Record a Sale.\nEnter 2 to Record a Purchase.\nEnter 3 to View Current Inventory.\nEnter 4 to View Monthly Report.")
        try: 
            # choice = input(f"{question}\nEnter 'q' to exit.\n")
            if choice is None:
                print("Exiting...")
                return
            elif choice == 1:
                record_sale("sales.csv")
            elif choice == 2:
                record_purchase("purchases.csv")
            elif choice == 3:
                view_inventory("inventory.csv")
            elif choice == 4:
                pass
            else:
                print("Please enter a valid choice between 1-4.")
        except ValueError as e:
            print("Error: ", e)

if __name__ == '__main__':
    main_menu()