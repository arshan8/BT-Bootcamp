from pytest import raises
from pydantic import ValidationError
import pytest

from Sequence_programming.code_Sequence_programming.Q_4 import Number , swap


def test_swap():
    # amount = 100, discount = 10% → discount value = 10
    assert swap(100, 10) == (10, 100)
   

def test_amount_model_invalid_string():
    with raises(ValidationError):
        Number(a = "10",b =  "abc")

