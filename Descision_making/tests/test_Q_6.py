from Descision_making.code.Q_6 import check_parity


def test_check_parity():
    assert check_parity(4) == "even"
    assert check_parity(7) == "odd"   

#python -m Descision_making.tests.test_Q_6 
#PS C:\Users\ARSHAN\Desktop\bt-bootcamp> python -m pytest Descision_making/tests/test_Q_6.py