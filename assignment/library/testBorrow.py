#653380042-6 พิทักษ์พงศ์ สุภาพเพ็ชร sec.2

import pytest
from main import Base, Borrowlist, User, Book

def test_add_borrowlist(db_session):
    user = User(username="test_user", fullname="Test User")
    book = Book(title="Test Book", firstauthor="Test Author", isbn="1234567890")
    
    db_session.add(user)
    db_session.add(book)
    db_session.commit()
   
    new_borrowlist = Borrowlist(user_id=user.id, book_id=book.id)
    db_session.add(new_borrowlist)
    db_session.commit()

    borrowed_book = db_session.query(Borrowlist).filter_by(user_id=user.id, book_id=book.id).first()
    assert borrowed_book is not None
    assert borrowed_book.user_id == user.id
    assert borrowed_book.book_id == book.id

def test_get_borrowlist(client, db_session):
    user = User(username="test_user", fullname="Test User")
    book = Book(title="Test Book", firstauthor="Test Author", isbn="1234567890")
    
    db_session.add(user)
    db_session.add(book)
    db_session.commit()
    
    new_borrowlist = Borrowlist(user_id=user.id, book_id=book.id)
    db_session.add(new_borrowlist)
    db_session.commit()

    response = client.get(f"/borrowlist/{user.id}")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["user_id"] == user.id
    assert data[0]["book_id"] == book.id
    assert "timestamp" in data[0]