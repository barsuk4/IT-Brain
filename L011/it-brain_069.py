class Book:
    def __init__(self, year, title, author, page_count):
        self.year = year
        self.title = title
        self.author = author
        self.page_count = page_count

    @staticmethod
    def count_books_by_year(book_list, target_year):
        """Повертає кількість книг, опублікованих у вказаному році."""
        return sum(1 for book in book_list if book.year == target_year)


# Приклад використання:

book1 = Book(2001, "Книга 1", "Автор 1", 300)
book2 = Book(2002, "Книга 2", "Автор 2", 350)
book3 = Book(2001, "Книга 3", "Автор 3", 400)
book4 = Book(2003, "Книга 4", "Автор 4", 200)

books = [book1, book2, book3, book4]

print(f"Кількість книг опублікованих у 2001 році: {Book.count_books_by_year(books, 2001)}")
