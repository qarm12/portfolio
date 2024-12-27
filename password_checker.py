# All possible characters that can be within a password (except escape sequences)
uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowercase = uppercase.lower()
symbols = "~`!@#$%^&*()_-+={}[]|:;'/>.<,"
numbers = "0123456789"
# Minimum Password Length
pass_len = 12
# Indicates whether each case if met or not

# Check for length
def Length(password):
    if len(password) < pass_len:
        return "This password must contain at least 12 characters."
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
        # This construction counts to make sure there are enough kinds of characters in the password
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
    symbol_evaluation = Symbols(password, symbols)
    number_evaluation = Numbers(password, numbers)

    return length_evaluation, uppercase_evaluation, lowercase_evaluation, symbol_evaluation, number_evaluation

# Suggested improvements
def Improvements(password):
    length_eval, upper_eval, lower_eval, symbol_eval, num_eval = evaluate_password(password)
    # Checks whether each case is True
    if length_eval[0:19] == "This password meets" and upper_eval[0:19] == "This password meets" and lower_eval[0:19] == "This password meets" and symbol_eval[0:19] == "This password meets" and num_eval[0:19] == "This password meets":
        return (f"'{password}' is a strong password. ")
    else:
        return f"{length_eval}\n{upper_eval}\n{lower_eval}\n{symbol_eval}\n{num_eval}"

password = input("Enter a password: ")
print(Improvements(password))
