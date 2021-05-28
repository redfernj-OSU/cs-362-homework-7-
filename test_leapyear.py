import pytest
import leapyear

def test_divby4():
    assert leapyear.leapyear(4) == True