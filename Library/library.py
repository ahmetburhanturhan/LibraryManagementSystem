class Library:
    def __init__(self) -> None:
        self.file = open("books.txt" , "a+", encoding="utf-8")

    def __del__(self):
        if self.file:
            self.file.close()

    def add_book(self):
        # Kullanıcıdan bilgileri al
        self.bilgi1 = input("Enter the book title: ")
        self.bilgi2 = input("Enter the author: ")
        self.bilgi3 = input("Enter the release year: ")
        self.bilgi4 = input("Enter the page of number: ")


        # Bilgileri tek bir satirda birlestir
        birlesik_bilgi = f"{self.bilgi1}, {self.bilgi2}, {self.bilgi3}, {self.bilgi4}\n"

        # Dosyayi ac ve birlestirilmis satiri .txt'ye yaz
        with open("books.txt", "a+") as dosya:
            dosya.write(birlesik_bilgi)

    def list_book(self):
        self.file.seek(0)  # Dosya imlecini baslangica tasi
        books = self.file.read().splitlines()
        if not books:
            print("No books available.")
        else:
            print("List of books:")
            for book in books:
                book_info = book.split(',')
                print("Title: {}, Author: {}".format(book_info[0], book_info[1]))

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)  # Dosya imlecini baslangica tasi
        books = self.file.read().splitlines()
        self.file.seek(0)  # Dosya imlecini baslangica tasi
        updated_books = []

        for book in books:
            if title_to_remove not in book:
                updated_books.append(book)

        self.file.truncate(0)
        self.file.seek(0)

        for book in updated_books:
            self.file.write(book + '\n')

        print(f"Book '{title_to_remove}' has been removed.")

lib = Library()

# Menu
while True:
    print("\n*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit(q)\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_book()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == 'q':
        del lib
        break
    else:
        print("Invalid choice. Please enter a valid option.")
