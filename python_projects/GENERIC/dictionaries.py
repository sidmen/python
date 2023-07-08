password = input("Enter a new password: ")

result = {}      # define a dictionary

if len(password) > 8:
    result["length"] = True      # equivalent of result.append(True) for lists
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["uppercase"] = uppercase

print(result)

if all(result.values()):            # all values to be checked for Truth, not the keys
    print("Strong Password")
else:
    print("Weak Password")