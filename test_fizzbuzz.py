import fizzbuzz
import pytest

def test_fizz():
    assert fizzbuzz.fizzbuzz(3) == "Fizz"

def test_buzz():
    assert fizzbuzz.fizzbuzz(5) == "Buzz"
