

def rmv_duplicates(items):
    # This for loop does nothing. You are looping through items, but you never use the val variable. You can remove the loop and just do the other two lines. -69 Aura
    # Or, in a single line -> return set(items)
    for val in items:
        result = set(items)
    return result

print(rmv_duplicates([1, 2, 3, 1, 4, 4, 5, 5]))
print(rmv_duplicates([4, 6, 4, 11,13, 11]))
print(rmv_duplicates([-1, 22, 37, 34, 37, -1, 33]))