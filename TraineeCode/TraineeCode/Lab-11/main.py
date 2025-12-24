from employee import Employee
from employee_report import EmployeeReport
from datetime import date
from role_builder import RoleBuilder


if __name__ == "__main__":

    n = int(input("Enter total number of EMployees: "))
    employees = []   

    for _ in range(n):
        emp = Employee()

    
        emp.emp_id = input("Enter Employee ID: ")
        emp.emp_name = input("Enter Employee Name: ")
        emp.basic = float(input("Enter Basic Salary: "))
        emp.hra = float(input("Enter HRA: "))
        emp.allowance_percentage = float(input("Enter Allowance Percentage: "))
        from role_builder import RoleBuilder

        roles = [f"{role.value}-{role.name}" for role in RoleBuilder]
        roles_prompt = ", ".join(roles)

        emp.role = int(input(f"Enter Role [{roles_prompt}]: "))


        
        employees.append(emp)

        
        print("Employee stored successfully. Total employees:", len(employees))


    report = EmployeeReport(date.today().strftime("%d/%m/%Y"))

    report.display_employees(employees)
