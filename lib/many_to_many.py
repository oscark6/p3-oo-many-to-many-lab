class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
        


# Example usage:
author1 = Author("daniel beyene")
author2 = Author("daniel beyene")

book1 = Book("Book 1")
book2 = Book("Book 2")

contract1 = author1.sign_contract(book1, "2022-01-01", 10)
contract2 = author2.sign_contract(book2, "2022-01-02", 20)
contract3 = author1.sign_contract(book2, "2022-01-03", 30)

print(author1.books())  # prints: [book1, book2]
print(book1.authors())  # prints: [author1]
print(author1.total_royalties())  # prints: 40
print(Contract.contracts_by_date("2022-01-01"))  # prints: [contract1]