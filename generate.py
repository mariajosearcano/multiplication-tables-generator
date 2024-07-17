import msvcrt

def tables():
    print("Enter the number from which to generate the table")
    numberString = input("=> ")
    print()

    number = int(numberString)

    print(f"MULTIPLICATION TABLE OF {number}")
    for i in range(13):
        print(f"{number} x {i} = {number * i}")

    print()
    print("Press a key to continue...")
    msvcrt.getch()