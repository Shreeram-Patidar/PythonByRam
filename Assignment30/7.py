"""
7.
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z.
"""

# =========================================
# MISSING ALPHABET FINDER
# =========================================

alphabets = set("abcdefghijklmnopqrstuvwxyz")
sentence = ""

while True:
    print("\n----- MISSING ALPHABET FINDER -----")
    print("1. Enter Sentence")
    print("2. Display Missing Alphabets")
    print("3. Count Missing Alphabets")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            sentence = input("Enter Sentence: ")
            print("Sentence Saved.")

        case 2:
            entered = set(sentence.lower())
            missing = alphabets - entered

            print("Missing Alphabets:", missing)

        case 3:
            entered = set(sentence.lower())
            missing = alphabets - entered

            print("Count of Missing Alphabets:", len(missing))

        case 4:
            print("Program Ended.")
            break

        case _:
            print("Invalid Choice")