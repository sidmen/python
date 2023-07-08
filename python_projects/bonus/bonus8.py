while True:
    try:
        width = float(input("Enter the width of rectangle: "))
        length = float(input("Enter the length of rectangle: "))

        if width == length:
            exit("That's a measurement of square. Exiting...")   # to exit the program with or without a message

        area = width * length
        print(f"Area of the rectangle is {area}")
        break           # Alternatively, exit() also works

    except ValueError:
        print("Please enter a number.")
        continue