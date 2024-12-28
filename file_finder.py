import subprocess

target_directory = "Flag"

def find():
    output_str = subprocess.getoutput("ls")

    # takes the files/directories in the current directory and checks to see if the flag is one of them
    output_lst = output_str.split()
    output = subprocess.getoutput(f"ls {target_directory}")

    for i in range(len(output_lst)):
        if output_lst[i] == target_directory:
            return subprocess.run(f"cat {target_directory}/{output}", shell=True)
    return FileNotFoundError

find()