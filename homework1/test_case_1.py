import pytest
from task1 import hello_world

def test_hello_world():
    assert hello_world() == "Hello, World!"

if __name__ == "__main__":
    pytest.main()
