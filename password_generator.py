import random

# Setting Possible Options
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "(){}[],:;,-_/\\?+*#"

# Decides Inclusive Characters
upper, lower, nums, syms = True, True, True, True

# Password String
all = ""

# Configuring Random Password
if upper:
  all += uppercase_letters
if lower:
  all += lowercase_letters
if nums:
  all += digits
if syms:
  all += symbols

# Setting Parameters for Password
length = input("Enter desired password length: ")
amount = 10

# Execution
password = "".join(random.sample(all, int(length)))
print("New Password: " + password)
