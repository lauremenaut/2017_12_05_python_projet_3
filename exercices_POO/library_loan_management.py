""" Models loan management system in a library """

import datetime


class Book:
    def __init__(self, title, reference):
        self.title = title
        self.reference = reference
        self.available = True


class Author:
    def __init__(self, name):
        self.name = name


class Reader:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def borrow_a_book(self, reference):
        pass


class Book_Author:
    def __init__(self, book_reference, *author_name):
        self.book_reference = book_reference
        self.author_name = author_name


class Loan:
    def __init__(self, book_reference, reader_name):
        self.book_reference = book_reference
        self.reader_name = reader_name
        self.loan_date = datetime.date.today()
        self.end_of_loan_date = self.loan_date + 30

class Library: # collection
    def __init__(self):
        pass

    def add_book(self, book):
        pass

    def del_book(self, book):
        pass
