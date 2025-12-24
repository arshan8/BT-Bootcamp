from salary_calculator import SalaryCalculator

class Employee:
    def __init__(self, emp_id, name, basic, hra, allowance_percentage):
        self._emp_id = emp_id                # protected 
        self._name = name                     
        self._basic = float(basic)           # protected 
        self._hra = float(hra)               # protected
        self.allowance_percentage = allowance_percentage  # via setter

    @property             #properties can be accessed outside the Class too (to calculate salary, or diaply in report), 
    def emp_id(self):    #but not changed because no setter is defined
        return self._emp_id
    
    @property
    def emp_name(self):
        return self._name

    @property
    def basic(self):
        return self._basic

    @property
    def hra(self):
        return self._hra



    @property
    def allowance_percentage(self):
        return self._allowance_percentage

    @allowance_percentage.setter
    def allowance_percentage(self, value):
        value = float(value)
        if not (0 <= value <= 100):
            raise ValueError("Allowance percentage must be between 0 and 100")
        self._allowance_percentage = value


    def get_salary(self):             
        """Encapsulation: hides SalaryCalculator from outside classes,  eg: employee report only knows abt Employee class not salary calculator
        so callers interact only with Employee, not the calculator logic   (Better design choice)"""
        return SalaryCalculator.get_salary(self)
    

    
    def get_allowance(self):
        return SalaryCalculator.get_allowance(self)
    
