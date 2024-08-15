#653380042-6 พิทักษ์พงศ์ สุภาพเพ็ชร sec.2

import pytest
from main import User


def test_add_user(db_session):
    new_user = User(username="test_newuser1")
    db_session.add(new_user)
    db_session.commit()

    user = db_session.query(User).filter_by(username="test_newuser1").first()
    assert user is not None

def test_delete_user(db_session):
    user = User(username="test_newuser2")
    db_session.add(user)
    db_session.commit()

    db_session.delete(user)
    db_session.commit()

    deleted_user = db_session.query(User).filter_by(username="test_newuser2").first()
    assert deleted_user is None
