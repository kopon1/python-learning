# Lists are an object that lets you make a sequence of objects. In Python you can make a list of mixed elements.
# You make lists using [ ]. If defining the elements manually, you separate them with , commas
list_of_strings = ["book", "apple", "bones"]
list_of_numbers = [2, 3.4, 590]
list_of_different_types = ["book", 34, person.address]

# Here are the most commonly used inbuilt List functions (https://www.w3schools.com/python/python_ref_list.asp)
list_of_strings.reverse()
# print(list_of_strings) outputs ["bones", "apple", "book"]



# Dictionaries are another very useful data structure you will probably use a lot. They have only two major rules
# 1 - They are made of pairs of Keys and Values a.k.a kvp (key value pairs)
# 2 - Keys MUST BE unique. There cannot be any duplicate keys, Python will throw an exception.
# Just like a real world dictionary, you will nver find the same word twice, but you might have two different words with the same meaning.
# Dicts are made with { } and you can manually define a kvp with the following syntax -> key: value

# They DO NOT CARE what type of object you use as a key AS LONG AS they are immutable. Meaning that you cannot use things that can be changed dynamically.
# So no lists or dictionaries can be used as keys of a dictionary. Strings and numbers are perfectly fine.
# The types of the values of said keys is completely up to you.
dict_one = {
    1: "book",
    2: "house",
    3: "mouse"
}
dict_two = {
    "apples": 4.5,
    "mice": 5000000,
    "bananas": 0.0001
}
dict_of_some_objects_properties_and_function_results = {
    "balls_number": input_to_int("How many balls do you have?"),
    "address_uppercase": person.address.upper(), # You can directly influence the person.address string with any of the string-related functions. Easy as it gets.
    "age": person.age,
    "number_of_wheels": vehicle.wheel_number
}



# The problem I asked you to solve involved using a dict to separate operations made by the calculator and order them by the timestamp they were created in.
# As stated above, the value associated with a key can be basically anything, so we can use lists.
# The timestamps are the keys (unique) and since we can have multiple operations made in the same single minute, we put them in a list
operations_dict = {
    "05/05/2025 13:20": ["3 + 1 = 4"],
    "05/05/2025 13:23": ["3 / 2 = 1.5"]
}

# The values are lists, but they only have a single string inside. No problem, we know how to add things with .append()
# To access the value associated with a specific key, you can use the key's name directly inside [ ]. For example:
print(operations_dict["05/05/2025 13:20"]) 
# The line above is calling a "getter" on the dictionary, getting the value for that key, which in turn is used as the argument for print()
# Thus, this print will output [3 + 1 = 4] onto the terminal. It prints the whole list, not just a string because the value on this key is a list, not a single string.

# To make it even more clear, lets append a second operation to that list, because both share the same timestamp.
operations_dict["05/05/2025 13:20"].append("10 * 3 = 30")
print(operations_dict["05/05/2025 13:20"]) # This will now print [3 + 1 = 4, 10 * 3 = 30]

# Effectively the dict now looks like this
# {
#     "05/05/2025 13:20": ["3 + 1 = 4", "10 * 3 = 30"],
#     "05/05/2025 13:23": ["3 / 2 = 1.5"]
# }


# Try to figure out these things in sequence:
# 1: how to make an empty dictionary when the program starts
# 2: check if the CSV file exists and fill the dictionary with its contents if it does
# 3: insert operations into the dictionary they happen 
# 4: writing that dictionary to the CSV when the program closes


# BONUS: make a menu to allow the user to see the history; basically printing the dictionary to the terminal in a readable format.