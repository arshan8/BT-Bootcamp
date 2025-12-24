from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        emp.emp_id = input("Enter ID: ")
        emp.emp_name = input("Enter name: ")
        emp.emp_gender = input("Enter gender: ")
        
        addr1 = Address()
        addr1.address_1 = input("Enter Address 1: ")
        addr1.address_2 = input("Enter Address 2: ")
        addr1.Pincode = input("Enter Pincode: ")
        addr1.city = input("city : ")

        emp.address = addr1

        

    @staticmethod
    def show_data(emp):
        print(" --Employee Details --->>>>")
        print(f"Employee ID   :  {emp.emp_id}")
        print(f"Employee Name      : {emp.emp_name}")
        print(f"Employee Gender  : {emp.emp_gender}")

        print("\n \n -- Address Details ---->>>")
        print(f"Address Line 1 : {emp.address.address_1}")
        print(f"Address Line 2 : {emp.address.address_2}")
        print(f"City    : {emp.address.city}")
        print(f"Pincode : {emp.address.Pincode}")
        print("\n \n \n")


        print(emp)
        print(emp.address)



if __name__ == "__main__":
    Program.main([])
