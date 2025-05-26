import csv
import helpers
from pathlib import Path
import datetime as dt


# Reads a CSV file and returns a list of dictionaries. Each dictionary represents a row, having the column headers (fieldnames) as keys and the cell values as values
def load_csv(filename: str) -> list:
    with open(filename, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=None) 
        contents_list = []
        for line in csv_reader:
            contents_list.append(line)
        return contents_list
    
    
# Takes a list of dictionaries (in the format described in load_inventory) and writes to a CSV file.
# Returns True or False depending on if the writing operation succeeded or not.
# ATTENTION: This should only happen once, when the program is shutdown.
def save_csv(filename: str, rows_list: list) -> bool:
    # Writes inventory dictionary back to inventory.csv
    with open(filename, "a") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=None)
        for line in rows_list:
            csv_writer.writerow(line)
    
    
# Takes the name of a ball and a quantity and registers a new sale (a new dictionary) on the sales object (the list read from the CSV).
# This new entry has the ball type, quantity purchased, and timestamp.
# ATTENTION: You can only sell balls that you currently have in stock!
# ATTENTION #2: DO NOT SAVE TO CSV DIRECTLY. Use the lists that were created by reading the CSVs!
def record_sale():
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
    amount = helpers.input_to_int(f"Enter how many {ball_type} would you like to buy.")
    if amount == int(amount):
        confirmation = input(f"You have purchased {amount} {ball_type}.\nDo you confirm?\nEnter 'Y' for Yes or 'N' for No.\n").upper()
        if confirmation == "Y":
            updt_inventory = [{ball_type:[monthly_report(),amount]}]
            try:
                save_csv("sales.csv", updt_inventory)
            except ValueError as e:
                print("Error: ", e)
        elif confirmation == "N":
            return
        else:
            print("Please enter Y or N.")
    else:
        print("Invalid amount. Please input a valid amount in whole numbers.")


# Takes in the name of a ball and a quantity and registers a new purchase (a new dictionary) on the purchases object (the list read from the CSV).
# This new entry has the ball type, quantity purchased, and timestamp.
# ATTENTION: You can only have 250 units max of any ball because the Big Balls Inc. warehouse is pretty small. A purchase that exceeds the stock capacity should not be allowed to happen and the user should be informed.
def record_purchase(ball, quantity):
    dict = {ball:[quantity, monthly_report()]}
    pass


# Print out current stock of all balls (from the lists).
def view_inventory():
    # with open("csv_files/inventory.csv", "r") as csv_file:
    #     csv_reader = csv.DictReader(csv_file)
    #     for line in csv_reader:
    #         print(line)
    pass


# Print out the monthly report for the given year-month combo. Ordered by day ascending.
def monthly_report():
    now = dt.datetime.now()
    return now.strftime("%m-%Y")
    