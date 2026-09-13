"""
8.
=========================================
ALLOWED CHARACTER VALIDATOR
=========================================

Allowed characters are:
A-Z, a-z, 0-9

Store allowed characters in a Frozen Set.

Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit

Requirements:
- Use Frozen Set.
- Username should contain only allowed characters.
"""

# =========================================
# ALLOWED CHARACTER VALIDATOR
# =========================================

allowed = frozenset(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
)

username = ""

while True:
    print("\n----- ALLOWED CHARACTER VALIDATOR -----")
    print("1. Enter Username")
    print("2. Validate Username")
    print("3. Display Allowed Characters")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            username = input("Enter Username: ")
            print("Username Saved.")

        case 2:
            valid = True

            for char in username:
                if char not in allowed:
                    valid = False
                    break

            if valid:
                print("Valid Username")
            else:
                print("Invalid Username")
                print("Only A-Z, a-z and 0-9 are allowed.")

        case 3:
            print("Allowed Characters:")
            print(allowed)

        case 4:
            print("Program Ended.")
            break

        case _:
            print("Invalid Choice")