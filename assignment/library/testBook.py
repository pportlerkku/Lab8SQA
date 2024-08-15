#653380042-6 พิทักษ์พงศ์ สุภาพเพ็ชร sec.2

import pytest
from main import Book

def test_add_book(db_session):
    new_book = Book(title="test_newBook1", firstauthor="Author1", isbn="1234567890")
    db_session.add(new_book)
    db_session.commit()

    book = db_session.query(Book).filter_by(title="test_newBook1").first()
    assert book is not None

def test_delete_book(db_session):
    new_book = Book(title="test_newBook2", firstauthor="Author2", isbn="0987654321")
    db_session.add(new_book)
    db_session.commit()

    db_session.delete(new_book)
    db_session.commit()

    deleted_book = db_session.query(Book).filter_by(title="test_newBook2").first()
    assert deleted_book is None
