for i in range(31):
    x = int(input("Enter the temperature: "))
    if (x < -273 or x > 50):
        print("ERROR!")
    elif (x < 0):
        print("Cold...")
    elif (x > 0):
        print("Warm")
    else:
        print("Zero")
