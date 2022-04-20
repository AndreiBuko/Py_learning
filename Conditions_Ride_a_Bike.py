day = int(input("Enter number of the day of the week: "))
if (day < 1 or day > 7):
    print("There is no such day.")
elif (day == 7):
    print("Today is the weekend. Going for a bike ride.")
else:
    print("Today is a weekday.")
    


