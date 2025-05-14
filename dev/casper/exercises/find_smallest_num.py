# def find_small_num(items):
#     return min(items)
# print(find_small_num([1, 2, 3, 4, 5, 5]))
# print(find_small_num([4, 6, 13, 11]))
# print(find_small_num([-1, 22, 33]))



def find_small_num(items):
    minimum = items[0]
    for num in items:
        if num < minimum:
            minimum = num
    return minimum

print(find_small_num([1, 2, 3, 4, 0, 5, 5]))
print(find_small_num([4, 6, 13, 1, 11]))
print(find_small_num([-1, 22, 33, -10]))