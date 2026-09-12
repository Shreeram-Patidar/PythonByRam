"""=====================================================================
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
"""

from typing import NamedTuple


# Define NamedTuple
class Book(NamedTuple):
    book_id: str
    title: str
    author: str
    price: int


# 1. Read N book records
books = []

n = int(input("Enter number of books: "))

for i in range(n):
    data = input().split()

    book_id = data[0]
    title = data[1]
    author = data[2]
    price = int(data[3])

    book = Book(book_id, title, author, price)
    books.append(book)


# 2. Display all book details
print("\nAll Book Details:")

for book in books:
    print(book.book_id, book.title,
          book.author, book.price)


# 3. Find the most expensive book
expensive = books[0]

for book in books:
    if book.price > expensive.price:
        expensive = book

print("\nMost Expensive Book:")
print(expensive.book_id, expensive.title,
      expensive.author, expensive.price)


# 4. Search books by author name
author_name = input("\nEnter Author Name: ")

print("\nBooks Written By", author_name + ":")

for book in books:
    if book.author == author_name:
        print(book.book_id, book.title,
              book.author, book.price)


# 5. Calculate average price
total = 0

for book in books:
    total = total + book.price

average = total / n

print("\nAverage Book Price:")
print(average)