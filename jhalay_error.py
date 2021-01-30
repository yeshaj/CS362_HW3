# User enters the year
while True:
    try:
        year = int(input("Enter the year to see if it's a leap year: "))

        # Leap Year Check
        if year % 4 == 0 and year % 100 != 0:
            print(year, "is a Leap Year")
        elif year % 100 == 0:
            print(year, "is not a Leap Year")
        elif year % 400 == 0:
            print(year, "is a Leap Year")
        else:
            print(year, "is not a Leap Year")
    except ValueError:
        print("That's not a valid number. Try again")
