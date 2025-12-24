from employee_report import EmployeeReport

from employee import Employee

class Program:
    @staticmethod
    def main(args):
        # Employee array to hold the employees' information
        employees = [None] * 1

        # Accept employee information from the user
        print("Enter employee information")

        for i in range(len(employees)):
            print("Employee No : " + str(i+1))
            print("Id : ")
            emp_id = input()

            print("Name : ")
            name = input()

            print("Basic : ")
            basic = input()

            print("HRA : ")
            hra = input()

            print("Percentage of Allowance : ")
            allowance_percentage = input()

        
            emp = Employee(emp_id, name, basic, hra, allowance_percentage)
            employees[i] = emp

            
            # Note: Original C# code does not assign Employee object to Employees array

        print("Enter the date of the report (dd/mm/yyyy) : ")
        report_date = input()

        report = EmployeeReport(report_date)

        report.display_employees(employees)

        input()

        print(employees)
        print(employees[i].basic)


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
