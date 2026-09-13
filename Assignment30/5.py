"""
5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed.
"""

# =========================================
# LIBRARY ISBN MANAGER
# =========================================

isbn = set()

while True:
    print("\n----- LIBRARY ISBN MANAGER -----")
    print("1. Add ISBN")
    print("2. Remove ISBN")
    print("3. Search ISBN")
    print("4. Display ISBN List")
    print("5. Count Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            number = input("Enter ISBN: ")

            if number in isbn:
                print("ISBN already exists. Duplicate not allowed.")
            else:
                isbn.add(number)
                print("ISBN added successfully.")

        case 2:
            number = input("Enter ISBN to remove: ")

            if number in isbn:
                isbn.remove(number)
                print("ISBN removed successfully.")
            else:
                print("ISBN not found.")

        case 3:
            number = input("Enter ISBN to search: ")

            if number in isbn:
                print("ISBN Found")
            else:
                print("ISBN Not Found")

        case 4:
            print("\nISBN List:")

            if len(isbn) == 0:
                print("No ISBNs available.")
            else:
                for number in isbn:
                    print(number)

        case 5:
            print("Total Books:", len(isbn))

        case 6:
            print("Program Ended.")
            break

        case _:
            print("Invalid Choice")