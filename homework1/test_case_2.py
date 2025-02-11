import pytest
from task2 import variables

def test_variables():
    assert isinstance(variables["integer"], int)
    assert isinstance(variables["float"], float)
    assert isinstance(variables["string"], str)
    assert isinstance(variables["boolean"], bool)
