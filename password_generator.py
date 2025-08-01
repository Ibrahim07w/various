import random
import string
def generate(min_len=10, num=True, char=True):
    letters = string.ascii_letters
    special = string.punctuation
    digits = string.digits
    characters = letters
    if num:
        characters += digits
    if char:
        characters += special
    criteria, has_num, has_char = False, False, False
    password = ''
    while len(password) < min_len or not criteria:
        new = random.choice(characters)
        password += new
        if new in digits:
            has_num = True
        if new in special:
            has_char = True
        if num:
            criteria = has_num
        if char:
            criteria = criteria and has_char
    print(password)      
length = input('enter minimum length of password : ')  
has_digits = input('do you want numbers in it (True/False) : ').title()
has_char = input('do you want special charchters in it (True/False) : ').title()
generate(length, has_digits, has_char)