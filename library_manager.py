class Book:
    def __init__(self, title, author, publication_year, genre, read_status):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.read_status = read_status

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year}) - Genre: {self.genre} - Read: {'Yes' if self.read_status else 'No'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        publication_year = int(input("Enter the publication year: "))
        genre = input("Enter the genre: ")
        read_status = input("Have you read this book? (yes/no): ").lower() == 'yes'
        new_book = Book(title, author, publication_year, genre, read_status)
        self.books.append(new_book)
        print(f"Book '{title}' added to the library.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def search_book(self):
        search_term = input("Enter the title or author to search: ")
        found_books = [book for book in self.books if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]
        if found_books:
            print("Found books:")
            for book in found_books:
                print(book)
        else:
            print("No books found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in the library:")
        for book in self.books:
            print(book)

    def display_statistics(self):
        total_books = len(self.books)
        if total_books == 0:
            print("No books in the library.")
            return
        read_books = sum(1 for book in self.books if book.read_status)
        percentage_read = (read_books / total_books) * 100
        print(f"Total books: {total_books}")
        print(f"Percentage of books read: {percentage_read:.2f}%")

    def menu(self):
        while True:
            print("\nLibrary Menu:")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")
            choice = input("Choose an option (1-6): ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                self.display_books()
            elif choice == '5':
                self.display_statistics()
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    library = Library()
    library.menu()
