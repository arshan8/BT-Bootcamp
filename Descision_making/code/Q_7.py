
class Candidate:
    def __init__(self, name: str,  salary: float):
        self.name = name
        self.salary = salary
    
    def is_taxable(self) -> bool:
        return self.salary > 3_00_000



if __name__ == "__main__":
    try:
        name = input("Enter candidate's name: ")
        salary = float(input("Enter candidate's annual salary: "))
        
        C1= Candidate(name, salary)
        
        if C1.is_taxable():
            print(f"{C1.name}'s salary of {C1.salary} is taxable.")
        else:
            print(f"{C1.name}'s salary of {C1.salary} is not taxable.")
    

    except ValueError:
        print("Invalid input: Please enter a valid number for salary.")