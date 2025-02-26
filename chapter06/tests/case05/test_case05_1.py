from src.case05.case05_1 import Book, Customer


def test_book():
    book = Book()

    book.add_reservation(Customer(name="s3ich4n"))

    assert len(book._reservations) == 1
