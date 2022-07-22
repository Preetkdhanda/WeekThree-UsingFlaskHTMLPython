import unittest

from modules.book import Book

class TestBook(unittest.TestCase):
    
    def setUp(self):

        self.book1 = Book("Think Like A Monk", "Jay Shetty", "Self development")
        self.book2 = Book("Milk and Honey", "Rupi Kaur", "Poetry")
        self.book3 = Book("The Sun and Her Flowers", "Rupi Kaur", "Poetry")
        self.book4 = Book("A Thousand Splendid Suns", "Khaled Houssini", "Fiction")

    def test_book_has_title(self):
        self.assertEqual("Think Like A Monk",self.book1.title)

    def test_book_has_author(self):
        self.assertEqual("Jay Shetty",self.book1.author)
