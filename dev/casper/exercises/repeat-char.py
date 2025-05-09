

def repeat_char(str: str) -> bool:
    for char in str:
        char = str[0].upper()
        str1 = f"{char}{str}{char}"
        return str1
    
print(repeat_char("red"))
print(repeat_char("green"))
print(repeat_char("blue"))