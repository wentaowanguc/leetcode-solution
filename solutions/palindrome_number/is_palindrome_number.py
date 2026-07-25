def is_palindrome_string_slicing(x: int) -> bool:
    if x < 0 :
        return False
        
    return str(x) == str(x)[::-1]
        

def is_palindrome_mathmatics(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
        
    reversed_number = 0
    original_number = x

    while original_number > 0:
        digit = original_number % 10
        reversed_number = reversed_number * 10 + digit
        original_number //= 10

    return reversed_number == x