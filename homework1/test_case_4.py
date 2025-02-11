import pytest
from task4 import calculate_discount

def test_calculate_discount():
    assert calculate_discount(100, 10) == 90.0
    assert calculate_discount(200.0, 20) == 160.0