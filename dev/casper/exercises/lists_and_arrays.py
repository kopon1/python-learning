
my_list = [1, 4, 39, 5, 20, 3]

def find_num_in_list():
    result= [ ]
    for item in my_list:
        if item == 5:
            break
        result.append(item)
        print(result)
            
            
find_num_in_list()