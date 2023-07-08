password_prompt = "Enter password: "
password = input(password_prompt)

while password != "pass123":
    print("Incorrect password!")
    password = input(password_prompt)

print("Password is correct!")
