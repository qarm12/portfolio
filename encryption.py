import random

plain_text = input('Enter plaintext: ')
cipher_text = ""
plain_text1 = ""

characters = "1234567890!@#$%^&*()~`_-+={[}]|qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM<,.>?/:;' "
char_key = "1234567890!@#$%^&*()~`_-+={[}]|qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM<,.>?/:;' "

char_key = list(char_key)
characters = list(characters)

random.shuffle(char_key)

for letter in plain_text:
    index = characters.index(letter)
    cipher_text += char_key[index]

print(f'Encrypted Message: {cipher_text}')

for letter in cipher_text:
    index = characters.index(letter)
    plain_text1 += char_key[index]

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '0123456789'
symbols = '(){}[],:;,-_/?+*#~`><|=!@$%^&'

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
length = 50
#amount = 10

# Execution
password = "".join(random.sample(all, length))
print('')
print(f"Key: {password}")

key = input('Enter key: ')
print('')
if key == password:
    print(f'Decrypted Message: {plain_text}')
else:
    print('Incorrect key.')
