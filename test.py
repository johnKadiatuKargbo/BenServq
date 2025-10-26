# tests.py
from operations import *

genres = ("Fiction", "Non-Fiction", "Sci-Fi")

def run_tests():
    books = {}
    members = []

    # Test 1: Add valid book
    result = add_book(books, "111", "Python 101", "John", "Fiction", 2, genres)
    assert "added" in result

    # Test 2: Add duplicate ISBN
    result = add_book(books, "111", "Duplicate", "Jane", "Fiction", 1, genres)
    assert "exists" in result

    # Test 3: Add invalid genre
    result = add_book(books, "112", "Unknown", "Doe", "Horror", 2, genres)
    assert "Invalid genre" in result

    # Test 4: Add and borrow book
    add_member(members, "M001", "Alice", "alice@mail.com")
    result = borrow_book(books, members, "M001", "111")
    assert "borrowed" in result

    # Test 5: Return book restores copies
    copies_before = books["111"]["total_copies"]
    result = return_book(books, members, "M001", "111")
    copies_after = books["111"]["total_copies"]
    assert copies_after == copies_before + 1
    print("✅ All tests passed successfully!")

if __name__ == "__main__":
    run_tests()