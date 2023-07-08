def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_inches = input("Enter feet and inches: ")

parsed_feet = parse(feet_inches)['feet']
parsed_inches = parse(feet_inches)['inches']

result = convert(parsed_feet, parsed_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")
