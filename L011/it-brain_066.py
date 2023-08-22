class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' автор: {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Added item must be an instance of Book class.")

    def __str__(self):
        return "\n".join(str(book) for book in self.books)


# Створення бібліотеки
library = Library()

# Додавання книг до бібліотеки
library.add_book(Book("Енеїда", "Іван Котляревський",1798))
library.add_book(Book("Лісова пісня", "Леся Українка",1911))
library.add_book(Book("Зачарована Десна", "Іван Драч", 1957))
library.add_book(Book("Тигролови", "Іван Багряний", 1951))
library.add_book(Book("Кобзар", "Тарас Шевченко", 1840))

# Виведення списку книг у бібліотеці
print(library)
