# demo.py
from operations import *

# Initialize sample data
genres = ("Fiction", "Non-Fiction", "Sci-Fi")

books = {}
members = []

# Add some books
print(add_book(books, "978001", "Python Basics", "John Doe", "Fiction", 3, genres))
print(add_book(books, "978002", "AI Fundamentals", "Jane Smith", "Non-Fiction", 2, genres))

# Add members
print(add_member(members, "M001", "Alice", "alice@email.com"))
print(add_member(members, "M002", "Bob", "bob@email.com"))

# Search for a book
print(search_book(books, "Python"))

# Borrow book
print(borrow_book(books, members, "M001", "978001"))
print(borrow_book(books, members, "M002", "978001"))

# Try borrowing when copies run out
print(borrow_book(books, members, "M001", "978001"))

# Return a book
print(return_book(books, members, "M001", "978001"))

# Show final data
print("\\nFinal books data:", books)
print("Final members data:",members)