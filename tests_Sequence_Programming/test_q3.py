from pytest import raises
from pydantic import ValidationError
import pytest

from code_Sequence_programming.Q_3 import Amount, calculate_discount


def test_calculate_discount():
    # amount = 100, discount = 10% → discount value = 10
    assert calculate_discount(100, 10) == pytest.approx(10.0)
   


def test_amount_model_invalid_string():
    with raises(ValidationError):
        Amount(total_amount=0, discount_percent=10)


def test_amount_model_negative_amount():
    with raises(ValidationError):
        Amount(total_amount=-100, discount_percent=10)


def test_amount_model_negative_discount():
    with raises(ValidationError):
        Amount(total_amount=100, discount_percent=-5)
