class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

# Пример:
if __name__ == "__main__":
    # Экземпляр книги
    book1 = Book("Ревность", "Ю Несбё", 2021)

    # Информация о книге
    print(book1.get_info())

    # Вторая книга
    book2 = Book("Портрет Дориана Грея", "Оскар Уайльд", 1890)
    print(book2.get_info())
