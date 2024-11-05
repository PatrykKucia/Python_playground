# Plik: test_math_functions.py
## aby urychomić ->python -m pytest test_math_functions.py

from math_functions import add

def test_add_positive_numbers():
    assert add(1, 2, 3) == 6
    assert add(10, 20, 30) == 60

def test_add_negative_numbers():
    assert add(-1, -2, -3) == -6

def test_add_mixed_numbers():
    assert add(-1, 5, -2, 3) == 5

def test_add_no_arguments():
    assert add() == 0