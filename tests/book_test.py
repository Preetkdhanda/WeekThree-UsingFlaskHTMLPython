import unittest

from modules.book import *
from modules.booklist import *

class TestBook(unittest.TestCase):
    
    def setUp(self):

        self.book1 = Book("Think Like A Monk", "Jay Shetty", "Self development")
        self.book2 = Book("Milk and Honey", "Rupi Kaur", "Poetry")
   
    def test_book_has_title(self):
        self.assertEqual("Think Like A Monk",self.book1.title)

    def test_book_has_author(self):
        self.assertEqual("Jay Shetty",self.book1.author)

    def test_how_many_books(self):
        add_book(self.book1)
        self.assertEqual(5,len(books))
        
    def test_if_book_removed(self):
         remove_book("Think Like A Monk")   
         self.assertEqual(4, len(books)) 
