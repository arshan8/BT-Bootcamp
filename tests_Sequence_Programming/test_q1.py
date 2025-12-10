from pytest import raises
from pydantic import ValidationError
from code_Sequence_programming.Q_1 import add, average, Number

def test_add():
    assert add(-5, 10) == 5

def test_average():
    assert average(20, 30) == 25

def test_invalid_numbers_model():
    with raises(ValidationError):
        Number(a="abc", b="20")
