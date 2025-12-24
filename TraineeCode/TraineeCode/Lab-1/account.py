class Account:
    """
    Fields for the class
    """                   #why class level objects? not necessary, just for readablity
    _acc_no =  None   #why no init??? because object is created empty, and must be filled by other class like account manager 1 or 2
    _name = None    # __init__ avoids forcing values early
    _balance = 0.    #No setter is called.

    """                              #If _balance were a mutable type like list, all objects would share it. which is dangerous

    Look in instance dictionary → self.__dict__
    If not found, look in class dictionary → Account.__dict__
    If still not found, look in parent classes 


    
    Properties for the fields
    """
    @property
    def acc_no(self):
        return self._acc_no

    @acc_no.setter
    def acc_no(self, value):
        bank_code = "ICI"
        self._acc_no = bank_code + value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def balance(self):
        return self._balance + self.compute_interest()

    @balance.setter
    def balance(self, value):
        self._balance = value

    """
    Method to calculate the interest for an account
    """
    """
    returns Interest
    """
    def compute_interest(self):
        interest = self._balance * 8.5 / 100.0
        return interest
