speed = int(input("Car speed: "))
if (speed > 200):
    print("This is not a plane, liar!")
elif (speed > 60):
    print("Driver violated the rules!")
elif (speed == 0):
    print("We are not going anywhere!")
elif (speed < 0):
    print("Negative speed doesn't exist!")
else:
    print("Driver is a good boy!")
