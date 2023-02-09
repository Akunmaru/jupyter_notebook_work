def Area():
    print("Welcome to AREA calculator! \ninput the required values\nand I will handle the rest!")
    while True:
        width = input("What is the width of the object? ")
        if width.lower() == 'quit': break
        length = input ("What is the length of the object? ")
        if length.lower() == 'quit': break
        Area = int(width) * int(length)
        print(Area)