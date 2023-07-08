import glob

myfiles = glob.glob("*.py")

print(myfiles)

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())