def strength(password):
    result = []

    if len(password) >= 8:
        result.append(True)
    else:
        result.append(False)

    print(result)

    for i in password:
        if i.isupper():
            result.append(True)

    print(result)

    for i in password:
        if i.isdigit():
            result.append(True)

    if all(result):
        message = "Strong Password"
    else:
        message = "Weak Password"

    return message

print(strength("Haaaaaapy888"))