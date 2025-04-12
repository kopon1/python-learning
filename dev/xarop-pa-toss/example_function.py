from myutils import input_int

ingredient_quantities = {
    "flour": 200,
    "egg": 12,
    "bread": 3,
    "chocolate": 30,
    "cheese": 5
}

recipes = {
    "chocolate cake": [
        ("flour", 50),
        ("egg", 6),
        ("chocolate", 20)
    ],
    "cheese toast": [
        ("bread", 1),
        ("cheese", 1)
    ],
    "french toast": [
        ("bread", 2),
        ("egg", 2)
    ],
    "scrambled eggs": [
        ("egg", 3),
        ("cheese", 1)
    ],
    "chocolate sandwich": [
        ("bread", 2),
        ("chocolate", 10)
    ],
    "cheesy omelette": [
        ("egg", 4),
        ("cheese", 2)
    ]
}


def menu():
    while True:    
        print("""
        *** Welcome to the cookbook ***
        1 - See recipe list
        2 - Cook recipe!!
        3 - Add recipe
        4 - Delete recipe
        5 - Check ingredients
        
        """ )
        
        menu_choice = input_int("Pick an option")
        
        match menu_choice:
            case None: 
                return
            case 4:
                delete_recipe() 

def delete_recipe():
    while True:
        print("Pick a recipe to delete:")
        for index, key in enumerate(recipes):
            print(f"{index}: {key}")
        
        # Chose to quit
        delete_choice = input_int(">>>")
        if delete_choice is None:
            return
        
        # Did not pick a valid number from the list
        keys_list = list(recipes)
        if delete_choice <= 0 or delete_choice >= len(keys_list):
            print("Invalid number. Pick a number from the recipe list.")
            continue
        
        del recipes[keys_list[delete_choice]]
        return
        
    
#as long as this function call is after all the functions, you are fine
menu()
print("quitting now!!!")