
my_list = [1, 4, 39, 5, 20, 3]

def find_num_in_list():
    result = []
    for x, element in enumerate(my_list):
        if element == 5:
            break
        elif 5 not in my_list:
            print("Num 5 not in list")
            return
        result.append(element)
    print(result)        
find_num_in_list()