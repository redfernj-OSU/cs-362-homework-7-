import fizzbuzz
import pytest

def test_fizz():
    assert fizzbuzz.fizzbuzz(3) == "Fizz"

def test_buzz():
    assert fizzbuzz.fizzbuzz(5) == "Buzz"

def test_fizzbuzz():
    assert fizzbuzz.fizzbuzz(15) == "FizzBuzz"

def test_else():
    assert fizzbuzz.fizzbuzz(19) == 19
