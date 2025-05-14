


def calc_mult(items):
    num = 1
    for val in items:
        num = val * num
    return num

print(calc_mult([1, 2, 3, 4, 5, 5]))
print(calc_mult([4, 6, 13, 11]))
print(calc_mult([-1, 22, 33]))