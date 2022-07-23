from modules.book import *
from tests.book_test import *

book1 = Book("Think Like A Monk", "Jay Shetty", "Self development")
book2 = Book("Milk and Honey", "Rupi Kaur", "Poetry")
book3 = Book("The Sun and Her Flowers", "Rupi Kaur", "Poetry")
book4 = Book("A Thousand Splendid Suns", "Khaled Houssini", "Fiction")

books = [book1, book2, book3, book4]

# books = []

## your functions are here because there are
## not suppose to be in the class section Preet!
## class file is ONLY suppose to have the class!

def add_book(book):
      books.append(book)
      return

def remove_book(removed_book):
     
      for book in books:
            if ["book.title"] == book:
              
             books.remove(removed_book)
             
      return


# def delete_event(event_name):
#     event_to_delete = None
#     for event in events:
#         if event.name == event_name:
#             event_to_delete = event
#             break
      
#         events.remove(event_to_delete)
# def delete_book(removed_book):
#       book = None
#       for book in books:
#         if removed_book == book:
#             books.remove(removed_book)