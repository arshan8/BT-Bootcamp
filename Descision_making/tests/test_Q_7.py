from Descision_making.code.Q_7 import Candidate

def test_if_taxable():
    C1 = Candidate(name = "Henry", salary =600000)
    assert C1.is_taxable() == True
    C2 = Candidate(name = "Tom", salary=20000)
    assert C2.is_taxable() == False


#from root dir
# PS C:\Users\ARSHAN\Desktop\bt-bootcamp> python -m Descision_making.tests.test_Q_7
# PS C:\Users\ARSHAN\Desktop\bt-bootcamp> python -m pytest Descision_making\tests\test_Q_7.py