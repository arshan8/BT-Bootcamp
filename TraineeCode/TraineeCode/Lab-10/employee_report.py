from employee import Employee



class EmployeeReport:
    """
    Property of the class
    """
    def __init__(self, date):
        self.report_date = date

    """
    Method to print a line in a report
    """
    def print_line(self):
        print("---------------------------------------------------------------------------")

    """
    Method to display header information of the report
    """
    def display_header(self):
        self.print_line()
        print("EMPLOYEE REPORT\t\t\t\t")
        print("Date : " + self.report_date)
        self.print_line()

    """
    Method to display footer information in the report
    """
    def display_footer(self, count):
        self.print_line()
        print("Total Employees : " + str(count))
        self.print_line()

    """
    Method to display employees information
    """
    def display_employees(self, employees):
        self.display_header()

        print("EMP_ID\tNAME\tBASIC\tHRA\tALLOW\tSALARY")
        for emp in employees:
      
            salary = emp.get_salary()             
            allowance = emp.get_allowance()
            print(
                f"{emp.emp_id}\t"
                f"{emp.emp_name}\t"
                f"{emp.basic}\t"
                f"{emp.hra}\t"
                f"{allowance}\t"
                f"{salary}"
            )
        self.print_line()

        # Placeholder for employee information printing
        # Original C# code does not include the loop for displaying details

        self.display_footer(len(employees))
