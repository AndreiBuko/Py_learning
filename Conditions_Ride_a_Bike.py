day = int(input("Enter number of the day of the week: "))
if (day == 7):
    print("Today is the weekend. Going for a bike ride.")
else:
    if (day < 1):
        print("There is no such day.")
    else:
        if (day > 7):
            print("There is no such day.")
        else:
            print("Today is a weekday.")
    


