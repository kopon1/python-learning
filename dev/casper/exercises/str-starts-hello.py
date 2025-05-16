


def check_str_starts_hello(word):
    if word.lower().startswith("hello"):
        return True
    else:
        return False
    
    
print(check_str_starts_hello("World Hello"))
print(check_str_starts_hello("Any words... hello world"))
print(check_str_starts_hello("hello world!"))
print(check_str_starts_hello("Hello World!"))