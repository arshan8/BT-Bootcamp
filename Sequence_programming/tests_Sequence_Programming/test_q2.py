from pytest import raises
from pydantic import ValidationError
from Sequence_programming.code_Sequence_programming.Q_2 import SimpleInterest, Number
import pytest

def test_SimpleInterest():
    assert SimpleInterest(1, 1,1) == pytest.approx(0.01)


def test_invalid_numbers_model():
    with raises(ValidationError):
        Number(a="abc", b= 20, c = 8)

def test_invalid_numbers_model():
    with raises(ValidationError):
        Number(a= -1, b= 20, c = 8)