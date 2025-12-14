from pydantic import BaseModel, Field, ValidationError

class EmployeeInput(BaseModel):

    name: str
    emp_id: str
    basic_monthly_salary: float = Field(ge=0)
    special_allowances: float = Field(ge=0, description="Monthly")
    
    annual_bonus_percent: float = Field(ge=0, le=100, description="Annual")


class SalaryCalculator:
    
    def __init__(self, employee_data: EmployeeInput):
        self.data = employee_data
        self.standard_deduction = 50_000
    
    @property
    def monthly_gross_salary(self):
        return (
            self.data.basic_monthly_salary +
            self.data.special_allowances
        )

    @property
    def annual_gross_salary(self):
        base_annual = self.monthly_gross_salary * 12
        return base_annual + (self.data.annual_bonus_percent / 100 * base_annual)

    def generate_gross_report(self):
        print(f"Employee name:           {self.data.name}")
        print(f"Employee id:             {self.data.emp_id}")
        print(f"Basic Monthly Salary:    ₹{self.data.basic_monthly_salary:,.2f}")
        print(f"special allowances:      ₹{self.data.special_allowances:,.2f}")
        print(f"annual Bonus (% of Gross): {self.data.annual_bonus_percent:.2f}%")
        print(f"monthly gross Salary:    ₹{self.monthly_gross_salary:,.2f}")
        print(f"annual Gross Salary:     ₹{self.annual_gross_salary:,.2f}")


    @property  # Q_12
    def annual_taxable_income(self):
        return max(0,self.annual_gross_salary - self.standard_deduction)

    def generate_taxable_report(self):
        print(f"Employee name:           {self.data.name}")
        print(f"annual Gross Salary:     ₹{self.annual_gross_salary:,.2f}")
        print(f"Standard_deduction:    ₹{self.standard_deduction:,.2f}")
        print(f"annual taxable Salary:     ₹{self.annual_taxable_income:,.2f}")


    @property
    def tax(self):   #progressive tax calculation
        income = self.annual_taxable_income

      
        if income <= 700_000:  #rebate
            return 0.0

        tax = 0.0
  
        if income > 300_000:
            tax += min(income - 300_000, 300_000) * 0.05
        if income > 600_000:
            tax += min(income - 600_000, 300_000) * 0.10
        if income > 900_000:
            tax += min(income - 900_000, 300_000) * 0.15
        if income > 1_200_000:
            tax += min(income - 1_200_000, 300_000) * 0.20
        if income > 1_500_000:
            tax += (income - 1_500_000) * 0.30

        return tax

    @property
    def cess(self):
        return self.tax * 0.04

    @property
    def total_tax(self):
        return self.tax + self.cess
    

    def display_tax_report(self):
        print(f"Employee name:           {self.data.name}")
        print(f"annual taxable Salary:     ₹{self.annual_taxable_income:,.2f}")
        print(f"Tax:                     ₹{self.tax:,.2f}")
        print(f"Cess:               ₹{self.cess:,.2f}")
        print(f"total tax:        ₹{self.total_tax:,.2f}")
      

    @property
    def net_annual_salary(self):
        return self.annual_gross_salary - self.total_tax
    
    
        


def run_challenge_1():
    print("Welcome to GlobalNext Solutions Tax Calculator.")
    
    input_data = {
        "name": "Sarah Connor",
        "emp_id": "GNS473",
        "basic_monthly_salary": 50000.00,
        "special_allowances": 20000.00,
        "annual_bonus_percent": 10.0 
    }
    
    try:
        
        employee_1 = EmployeeInput(**input_data)
        calculator = SalaryCalculator(employee_1)
        
        calculator.generate_gross_report()

        # employee_1.basic_monthly_salary = 10  #handles changes effieicently
        # calculator.generate_gross_report()

        calculator.generate_taxable_report()


        calculator.display_tax_report()

    except ValidationError as e:
    
        print("Invalid data")
        print(e)
        
    except ValueError as e:
        print("calculation error")
        print(e)


if __name__ == "__main__":
    run_challenge_1()