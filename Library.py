library = {}
users = {}

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    library[book_id] = {
        "title": title,
        "author": author,
        "available": True,
        "issued_to": None,
        "issue_day": None
    }

    print("✅ Book added successfully!\n")


def view_books():
    if not library:
        print("No books available.\n")
        return

    for book_id in library:
        book = library[book_id]
        status = "Available" if book["available"] else "Issued"

        print("ID:", book_id)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Status:", status)
        print("------------------------")
    print()


def register_user():
    user_id = input("Enter User ID: ")
    name = input("Enter User Name: ")

    users[user_id] = {"name": name}

    print("✅ User registered successfully!\n")


def issue_book():
    book_id = input("Enter Book ID to issue: ")
    user_id = input("Enter User ID: ")

    if book_id not in library:
        print("❌ Book not found.\n")
        return

    if user_id not in users:
        print("❌ User not found.\n")
        return

    if not library[book_id]["available"]:
        print("❌ Book already issued.\n")
        return

    issue_day = int(input("Enter issue day (number): "))

    library[book_id]["available"] = False
    library[book_id]["issued_to"] = user_id
    library[book_id]["issue_day"] = issue_day

    print("📕 Book issued successfully!\n")


def return_book():
    book_id = input("Enter Book ID to return: ")

    if book_id not in library:
        print("❌ Book not found.\n")
        return

    if library[book_id]["available"]:
        print("❌ Book was not issued.\n")
        return

    return_day = int(input("Enter return day (number): "))
    issue_day = library[book_id]["issue_day"]

    days_used = return_day - issue_day
    fine = 0

    if days_used > 7:
        fine = (days_used - 7) * 5

    library[book_id]["available"] = True
    library[book_id]["issued_to"] = None
    library[book_id]["issue_day"] = None

    print("🔁 Book returned successfully!")

    if fine > 0:
        print("💰 Late fine: ₹", fine)
    else:
        print("No fine.")

    print()

def main():
    while True:
        print("📚 LIBRARY MANAGEMENT SYSTEM")
        print("1. Add Book ➕📚")
        print("2. View Books 📖")
        print("3. Register User 👤")
        print("4. Issue Book 📕")
        print("5. Return Book 🔁")
        print("6. Exit 🚪")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            register_user()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank you for using Library System 📚")
            break
        else:
            print("Invalid choice!\n")


main()