import pytest
from task7 import fetch_data

def test_fetch_data():
    assert fetch_data("https://www.google.com") == 200
