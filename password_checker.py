# Password Checking Program
uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowercase = uppercase.lower()
symbol_s = "~`!@#$%^&*()_-+={}[]|\:;'/>.<,"
numbers = "0123456789"


# Check for length
def Length(password):
    if len(password) < 12:
        return "This password must contain at least 12 unique characters."
    else:
        return "This password meets the length requirement."


# Check for uppercase
def Uppercase(password, uppercase):
    count = sum(1 for char in password if char in uppercase)
    for x in password:
      if count < 3 or (password.count(x) > 1 and count < 3):
        return "This password must contain at least 3 unique uppercase characters."
      else:
        return "This password meets the uppercase requirement."


# Check for lowercase
def Lowercase(password, lowercase):
    count = sum(1 for char in password if char in lowercase)
    for y in password:
      if count < 3 or (password.count(y) > 1 and count < 3):
        return "This password must contain at least 3 unique lowercase letters."
      else:
        return "This password meets the lowercase requirement."


# Check for Symbols
def Symbols(password, symbol):
    count = sum(1 for char in password if char in symbol)
    for z in password:
      if count < 3 or (password.count(z) > 1 and count < 3):
        return "This password must contain at least 3 unique symbols."
      else:
        return "This password meets the symbol requirement."

def Numbers(password, numbers):
    count = sum(1 for char in password if char in numbers)
    for u in password:
      if count < 3 or (password.count(u) > 1 and count < 3):
        return "This password must contain at least 3 unique numbers."
      else:
        return "This password meets the number requirement."


# Overall Rating/Evaluation of Password
def evaluate_password(password):
    length_evaluation = Length(password)
    uppercase_evaluation = Uppercase(password, uppercase)
    lowercase_evaluation = Lowercase(password, lowercase)
    symbol_evaluation = Symbols(password, symbol_s)
    number_evaluation = Numbers(password, numbers)

    return length_evaluation, uppercase_evaluation, lowercase_evaluation, symbol_evaluation, number_evaluation


# Suggested improvements
def Improvements(password):
    length_eval, uppercase_eval, lowercase_eval, symbol_eval, number_eval = evaluate_password(password)
    print(length_eval)
    print(uppercase_eval)
    print(lowercase_eval)
    print(symbol_eval)
    print(number_eval)


password = "RandPassword.password"
Improvements(password)