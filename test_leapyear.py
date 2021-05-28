import pytest
import leapyear

def test_divby4():
    assert leapyear.leapyear(4) == True

def test_divby100():
    assert leapyear.leapyear(100) == True

def test_divby400():
    assert leapyear.leapyear(400) == True

def test_other():
    assert leapyear.leapyear(2019) == False