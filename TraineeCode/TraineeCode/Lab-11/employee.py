from salary_calculator import SalaryCalculator
from role_builder import RoleBuilder

class Employee:
    def __init__(self):
        # default  object
        self._emp_id = None
        self._name = None
        self._basic = 0.0
        self._hra = 0.0
        self._allowance_percentage = 0.0
        self._role = None

    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value

    @property
    def emp_name(self):
        return self._name

    @emp_name.setter
    def emp_name(self, value):
        self._name = value

    @property
    def basic(self):
        return self._basic

    @basic.setter
    def basic(self, value):
        self._basic = float(value)

    @property
    def hra(self):
        return self._hra

    @hra.setter
    def hra(self, value):
        self._hra = float(value)

    @property
    def allowance_percentage(self):
        return self._allowance_percentage

    @allowance_percentage.setter
    def allowance_percentage(self, value):
        value = float(value)
        if not (0 <= value <= 100):
            raise ValueError("Allowance percentage must be between 0 and 100")
        self._allowance_percentage = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        try:
        # validate against enum automatically
            self._role = RoleBuilder(int(value)).value
        except ValueError:
            raise ValueError("Invalid role id")

    def get_salary(self):
        return SalaryCalculator.get_salary(self)

    def get_allowance(self):
        return SalaryCalculator.get_allowance(self)

    def get_role_description(self):
        return RoleBuilder(self.role).name
