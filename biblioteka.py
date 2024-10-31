class Book:
  def __init__(self, title, author):
      self.title = title
      self.author = author

  def __str__(self):
      return f"'{self.title}' by {self.author}"

class Library:
  def __init__(self):
      self.books = []

  def add_book(self, title, author):
      """Добавляет новую книгу в библиотеку."""
      new_book = Book(title, author)
      self.books.append(new_book)
      print(f"Книга {new_book} добавлена в библиотеку.")

  def remove_book(self, title):
      """Удаляет книгу по названию."""
      for book in self.books:
          if book.title.lower() == title.lower():
              self.books.remove(book)
              print(f"Книга '{book.title}' удалена из библиотеки.")
              return
      print(f"Книга с названием '{title}' не найдена.")

  def display_books(self):
      """Выводит список всех книг в библиотеке."""
      if not self.books:
          print("Библиотека пуста.")
      else:
          print("Книги в библиотеке:")
          for book in self.books:
              print(book)

  def find_book(self, title):
      """Ищет книгу по названию."""
      for book in self.books:
          if book.title.lower() == title.lower():
              print(f"Книга найдена: {book}")
              return
      print(f"Книга с названием '{title}' не найдена.")

def main():
  library = Library()
  while True:
      print("\nСимулятор Библиотеки:")
      print("1. Добавить книгу")
      print("2. Удалить книгу")
      print("3. Показать все книги")
      print("4. Найти книгу по названию")
      print("5. Выйти")

      choice = input("Выберите действие (1-5): ")

      if choice == "1":
          title = input("Введите название книги: ")
          author = input("Введите автора книги: ")
          library.add_book(title, author)
      elif choice == "2":
          title = input("Введите название книги для удаления: ")
          library.remove_book(title)
      elif choice == "3":
          library.display_books()
      elif choice == "4":
          title = input("Введите название книги для поиска: ")
          library.find_book(title)
      elif choice == "5":
          print("Выход из программы.")
          break
      else:
          print("Неверный выбор, попробуйте еще раз.")

if __name__ == "__main__":
  main()