print("""Name a number that
is not less than 80 and not greater than 150
and not less than 90 or equal to 150""")

x = int(input("Enter the number: "))

res = (not(x < 80) and not(x > 150) \
       and not(x <90) or (x == 150))

if (res):
    print("You guessed it!")
else:
    print("Unfortunately no...")

input("Press ENTER to exit...")
quit()
