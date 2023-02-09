def Area():
    print("Welcome to AREA calculator!")
    while True:
        width = input("What is the width of the object? ")
        if width.lower() == 'quit': break
        length = input ("What is the length of the object? ")
        if length.lower() == 'quit': break
        Area = int(width) * int(length)
        print(Area)



def Circumfrence():
    print("Welcome to CIRCUMFRENCE calculator!")
    while True:
        print("If you do not have the Diameter type, 'skip' \n if you want to end program type, 'quit'")
        diam = input("What is the DIAMETER of your circle? ")
        if diam == 'quit': break
        if diam != 'skip': 
            radius = int(diam) / 2
            circum = 2 * 3.14 * radius
            print(circum)
        if diam == 'skip': 
            rad = input("What is the RADIUS of your circle? ")
            if rad == 'quit':
                break
            circum =  2 * 3.14 * int(rad)
            print(circum)
Circumfrence()