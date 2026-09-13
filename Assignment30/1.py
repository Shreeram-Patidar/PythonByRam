"""
1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.
"""

coding = set()
robotics = set()

while True:
    print("\n===== STUDENT CLUB MEMBERSHIP SYSTEM =====")
    print("1. Add Student to Coding Club")
    print("2. Add Student to Robotics Club")
    print("3. Display Students in Coding Club")
    print("4. Display Students in Robotics Club")
    print("5. Find Students in Both Clubs")
    print("6. Find Students Only in Coding Club")
    print("7. Find Students Only in Robotics Club")
    print("8. Display All Unique Club Members")
    print("9. Display Total Unique Club Members")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student = input("Enter Student ID: ")
        coding.add(student)
        print("Student added to Coding Club.")

    elif choice == 2:
        student = input("Enter Student ID: ")
        robotics.add(student)
        print("Student added to Robotics Club.")

    elif choice == 3:
        print("Coding Club Students:", coding)

    elif choice == 4:
        print("Robotics Club Students:", robotics)

    elif choice == 5:
        both = coding.intersection(robotics)
        print("Students in Both Clubs:", both)

    elif choice == 6:
        only_coding = coding.difference(robotics)
        print("Only in Coding Club:", only_coding)

    elif choice == 7:
        only_robotics = robotics.difference(coding)
        print("Only in Robotics Club:", only_robotics)

    elif choice == 8:
        all_members = coding.union(robotics)
        print("All Unique Members:", all_members)

    elif choice == 9:
        all_members = coding.union(robotics)
        print("Total Unique Members:", len(all_members))

    elif choice == 10:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
