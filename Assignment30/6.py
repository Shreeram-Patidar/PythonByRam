"""
6.

=========================================
COMMON CHARACTER FINDER
=========================================

Enter two strings and find common characters.

Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit

Example:
String1: python
String2: typhoon

Output:
{p, t, h, o, n}
"""

# =========================================
# COMMON CHARACTER FINDER
# =========================================

string1 = ""
string2 = ""

while True:
    print("\n----- COMMON CHARACTER FINDER -----")
    print("1. Enter First String")
    print("2. Enter Second String")
    print("3. Display Common Characters")
    print("4. Count Common Characters")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            string1 = input("Enter First String: ")
            print("First String Saved.")

        case 2:
            string2 = input("Enter Second String: ")
            print("Second String Saved.")

        case 3:
            common = set(string1) & set(string2)
            print("Common Characters:", common)

        case 4:
            common = set(string1) & set(string2)
            print("Count of Common Characters:", len(common))

        case 5:
            print("Program Ended.")
            break

        case _:
            print("Invalid Choice")