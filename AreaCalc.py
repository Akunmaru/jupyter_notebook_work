def Area():
    print("Welcome to AREA calculator! \n enter 'quit' to end.")
    while True:
        width = input("What is the width of the object? ")
        if width.lower() == 'quit': break
        length = input ("What is the length of the object? ")
        if length.lower() == 'quit': break
        Area = int(width) * int(length)
        print(Area)