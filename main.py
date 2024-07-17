
from generate import tables

print()
print("🔍 Welcome to the multiplication tables generator 🥸")

def about():
    print("Multiplication tables generator")
    print("Versión: 1.0")
    print("Autor: Maria Jose Arcila Cano")

selection = ""
while selection != "0":
    print()
    print("   🔢   ✖️   🔢   ")
    print()
    print("👇 Choose an option:")
    print("1. 🧮 Generate a table")
    print("2. ❓ About")
    print("0. 🚪 Exit")
    selection = input("=> ")
    print()

    match selection:
        case "1":
            tables()
        case "2":
            about()
        case "0":
            print("Until next time 👋")
            print()
        case _:
            print("Invalid option ❌")


