import pytest
from task5 import books, students

def test_books():
    assert len(books[:3]) == 3

def test_students():
    assert students["Ruben"] == 101