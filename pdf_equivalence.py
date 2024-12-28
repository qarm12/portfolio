one_file = input("Enter a filename: ")
two_file = input("Enter a filename: ")
equivalence = False
with open(one_file, "r") as file_one:
    with open(two_file, "r") as file_two:
        file1 = str(file_one.read())
        file2 = str(file_two.read())
        print(f'\nContents of {one_file}: "{file1}"\nContents of {two_file}: "{file2}"')
        if len(file1) == len(file2):
            for i in range(len(file1)):
                if file1 == file2:
                    equivalence = True
if equivalence == True:
    print(f"{one_file} and {two_file} are equivalent.\n")
else:
    print(f"{one_file} and {two_file} aren't equivalent.\n")
