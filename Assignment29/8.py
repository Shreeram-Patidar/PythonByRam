"""8.
MATRIX PATTERN DETECTION SYSTEM

A satellite monitoring center stores signal strengths in matrix form. Engineers want to identify special patterns in the matrix.

Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit
Requirements
Choice 1 – Count Even Numbers Above Main Diagonal

Count all even numbers where:

column > row
Choice 2 – Count Odd Numbers Below Main Diagonal

Count all odd numbers where:

row > column
Choice 3 – Display Boundary Elements

Display all elements present on:

First Row
Last Row
First Column
Last Column

without repeating corner elements.

Sample Input
1 2 3
4 5 6
7 8 9
Output
Even Numbers Above Main Diagonal = 2
(2, 6)

Odd Numbers Below Main Diagonal = 1
(7)

Boundary Elements:
1 2 3 6 9 8 7 4
"""

# MATRIX PATTERN DETECTION SYSTEM

# Read matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)


while True:

    print("\nMENU")
    print("1. Count Even Numbers Above Main Diagonal")
    print("2. Count Odd Numbers Below Main Diagonal")
    print("3. Display Boundary Elements")
    print("4. Exit")

    choice = int(input("Enter your choice: "))


    # Choice 1: Even numbers above main diagonal
    if choice == 1:

        count = 0
        even_numbers = []

        for i in range(rows):
            for j in range(cols):

                if j > i and matrix[i][j] % 2 == 0:
                    count = count + 1
                    even_numbers.append(matrix[i][j])

        print("Even Numbers Above Main Diagonal =", count)
        print(tuple(even_numbers))


    # Choice 2: Odd numbers below main diagonal
    elif choice == 2:

        count = 0
        odd_numbers = []

        for i in range(rows):
            for j in range(cols):

                if i > j and matrix[i][j] % 2 != 0:
                    count = count + 1
                    odd_numbers.append(matrix[i][j])

        print("Odd Numbers Below Main Diagonal =", count)
        print(tuple(odd_numbers))


    # Choice 3: Boundary elements
    elif choice == 3:

        boundary = []

        # First row
        for j in range(cols):
            boundary.append(matrix[0][j])

        # Last column (without first and last corner)
        for i in range(1, rows - 1):
            boundary.append(matrix[i][cols - 1])

        # Last row (right to left, without corners)
        for j in range(cols - 2, 0, -1):
            boundary.append(matrix[rows - 1][j])

        # First column (bottom to top, without corners)
        for i in range(rows - 2, 0, -1):
            boundary.append(matrix[i][0])

        print("Boundary Elements:")
        print(*boundary)


    # Choice 4: Exit
    elif choice == 4:

        print("Program Ended.")
        break


    else:
        print("Invalid Choice!")