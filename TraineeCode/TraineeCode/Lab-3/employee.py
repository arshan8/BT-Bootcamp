"""
Class to represent employee information
"""
from address import Address

class Employee:
    def __init__(self):
        self.__emp_id = None
        self.__emp_name = None
        self.__emp_gender = None
        self.__address = Address()

    @property
    def emp_id(self):
        return self.__emp_id

    @emp_id.setter
    def emp_id(self, emp_id):
        self.__emp_id = emp_id

    @property
    def emp_name(self):
        return self.__emp_name

    @emp_name.setter
    def emp_name(self, emp_name):
        self.__emp_name = emp_name

    @property
    def emp_gender(self):
        return self.__emp_gender

    @emp_gender.setter
    def emp_gender(self, emp_gender):
        self.__emp_gender = emp_gender

#Read only for address
    @property
    def address(self):
        return self.__address

    
    @address.setter
    def address(self, obj):
        if isinstance(obj, Address):
            self.__address = obj
        else:
            raise ValueError("only address expected: ")
