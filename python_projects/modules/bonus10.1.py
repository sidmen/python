from modules.parsers import parse, convert

feet_inches = input("Enter feet and inches: ")

parsed_feet = parse(feet_inches)['feet']
parsed_inches = parse(feet_inches)['inches']

result = convert(parsed_feet, parsed_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")
