from Descision_making.code.Q_9 import check_leap_year
import pytest

def test_check_leap_year():
    assert check_leap_year(2020) == True
    assert check_leap_year(1900) == False
    assert check_leap_year(2000) == True
    assert check_leap_year(2021) == False

def test_invalid_year():
    with pytest.raises(ValueError):
        check_leap_year(-10)