from pydantic import BaseModel, Field, ValidationError
import pandas as pd


class EmployeeInput(BaseModel):

    name: str
    emp_id: str
    basic_monthly_salary: float = Field(ge=0, le = 1_00_000, description="Monthly")
    special_allowances: float = Field(ge=0, le = 1_00_000, description="Monthly")
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

    
    @property  # Q_12
    def annual_taxable_income(self):
        return max(0,self.annual_gross_salary - self.standard_deduction)


    #Q 13
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
    

    #Q 14
    @property
    def net_annual_salary(self):
        return self.annual_gross_salary - self.total_tax
    

    #Q15

    def print_report(self):
        
        value = [
            self.data.name,
            self.data.emp_id,
            self.monthly_gross_salary,
            self.annual_gross_salary,
            self.annual_taxable_income,
            self.tax,
            self.cess,
            self.annual_taxable_income - self.tax - self.cess
            ]
        

        index = [
            "Name",
            "Emp ID",
            "Monthly Gross Salary",
            "Annual Gross Salary",
            "Annual Taxable Income",
            "Tax",
            "Cess (4%)",
            "Net Annual Salary"
        ]

        df = pd.DataFrame(value, index=index)
        print(df)
        

def run_challenge_1():
    print("Welcome to GlobalNext Solutions Tax Calculator.")
    
    while True:
        try:
            
            input_data = {
                "name" : input("Enter Employee Name: "),
                "emp_id": input("Enter Emp id: "),
                "basic_monthly_salary": input("Enter monthly salary: "),
                "special_allowances": input("Enter special allownace: "),
                "annual_bonus_percent": input("Enter bonus percent: ")
            }
        
            employee_1 = EmployeeInput(**input_data)
            break
            
        except ValidationError as e:  #input data validation
        
            print("Invalid data")
            print("Please re-enter the details correctly.\n")
            print(e)
        
    try:
        calculator = SalaryCalculator(employee_1)
        calculator.print_report()

    except ValueError as e:      #calculation errors
        print("calculation error")
        print(e)


if __name__ == "__main__":
    run_challenge_1()