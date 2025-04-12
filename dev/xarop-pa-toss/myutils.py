#myutils.py
def input_int(question):
    while True:
        choice = input(question + "\nPress 'q' to quit...\n>>> ")
        if choice.isdigit():
            return int(choice)
        elif choice == 'q':
            return None
        else:
            print("Choice must be a whole number. Try again...")   
            