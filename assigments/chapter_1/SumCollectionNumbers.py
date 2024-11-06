number = 1
summa = 0

while number != "0":
    number = input()

    try:
        summa += float(number)
        if number != "0":
            print(f"The total is now {summa}")
    except ValueError:
        print("That wasn’t a number.")

print(f"The grand total is {summa}")
