from Descision_making.code.Q_8 import largest_of_three

def test_largest_of_three():
    assert largest_of_three(10, 20, 15) == 20
    assert largest_of_three(-5, -1, -3) == -1
    assert largest_of_three(0, 0, 0) == 0
