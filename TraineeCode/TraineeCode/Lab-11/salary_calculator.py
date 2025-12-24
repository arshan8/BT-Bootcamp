class SalaryCalculator:
    """
    Method to calculate the salary of an employee
    """
    @staticmethod
    def get_salary(emp):
        salary = emp.hra + emp.basic + SalaryCalculator.get_allowance(emp)

        # Original python code has no calculation here

        return salary

    """
    Method to get the allowance for an employee based on the percentage
    """
    @staticmethod
    def get_allowance(emp):
        allowance = (emp.basic * emp.allowance_percentage / 100.0)
        return allowance


