class Address:
    
    def __init__(self):
        self.__address_1 = None
        self.__address_2 = None
        self.__Pincode = None
        self.__city = None


    @property
    def address_1(self):
        return self.__address_1
    
    @address_1.setter
    def address_1(self,val):
        self.__address_1 = val

    @property
    def address_2(self):
        return self.__address_2
    
    @address_2.setter
    def address_2(self,val):
        self.__address_2 = val

    @property
    def Pincode(self):
        return self.__Pincode
    
    @Pincode.setter
    def Pincode(self,val):
        try:
            self.__Pincode = int(val)
        except Exception :
            raise ValueError("Invalid Pincode")

    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self,val):
        self.__city = val