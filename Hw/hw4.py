class Book:
    default_format = "бумажная" # по умолчанию

    def __init__(self, title, author, pages, format=None):
        self.title = title
        self.author = author
        self.pages = pages
        self.format = format if format is not None else self.default_format

    def __str__(self): # магический метод для строкового представления объекта
        return f'"{self.title}" — {self.author}, {self.pages} стр.'

    def __len__(self): # магический метод для получения длины объекта
        return self.pages

    def __add__(self, other): # Магический метод для сложения двух книг
        total_pages = self.pages + other.pages
        return f"Вместе: {total_pages} страниц"

    def __eq__(self, other): # магический метод для сравнения двух книг
        return self.pages == other.pages

    def __getitem__(self, key): # магический метод для доступа по индексу
        return f"Глава {key}: содержание книги '{self.title}'"

    @classmethod # классовый метод для создания объекта из строки
    # использует cls для создания нового объекта
    def from_string(cls, s): # общепринято называть s от string
        parts = s.split(", ") #  разбиваем строку по запятой с пробелом
        title = parts[0]
        author = parts[1]
        pages = int(parts[2])
        return cls(title, author, pages)

    @staticmethod # статический метод для проверки, является ли книга толстой
    def is_thick(pages):
        return pages > 500

book1 = Book("1984", "Дж. Оруэлл", 328)
book2 = Book.from_string("Гарри Поттер, Дж. Роулинг, 400")

print(book1)
print(len(book1))
print(book1 + book2)
print(book1 == book2)
print(book1[5])

print(Book.is_thick(600))
print(Book.is_thick(300))

book3 = Book("Python", "Гвидо", 200)
print(book3.format)

