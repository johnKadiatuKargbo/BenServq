# operations.py

def add_book(books, isbn, title, author, genre, total_copies, genres):
    if isbn in books:
        return "Book with this ISBN already exists."
    if genre not in genres:
        return "Invalid genre. Allowed genres: " + ", ".join(genres)
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies
    }
    return f"Book '{title}' added successfully."

def add_member(members, member_id, name, email):
    for member in members:
        if member["member_id"] == member_id:
            return "Member with this ID already exists."
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return f"Member '{name}' added successfully."

def search_book(books, keyword):
    result = [book for book in books.values() if keyword.lower() in book["title"].lower()]
    return result if result else "No books found."

def borrow_book(books, members, member_id, isbn):
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        return "Member not found."
    if isbn not in books:
        return "Book not found."
    if books[isbn]["total_copies"] <= 0:
        return "No copies left."
    if len(member["borrowed_books"]) >= 3:
        return "Borrowing limit reached."
    books[isbn]["total_copies"] -= 1
    member["borrowed_books"].append(isbn)
    return f"Book '{books[isbn]['title']}' borrowed successfully."

def return_book(books, members, member_id, isbn):
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        return "Member not found."
    if isbn not in member["borrowed_books"]:
        return "This book was not borrowed by this member."
    member["borrowed_books"].remove(isbn)
    books[isbn]["total_copies"] += 1
    return f"Book '{books[isbn]['title']}' return successfully."