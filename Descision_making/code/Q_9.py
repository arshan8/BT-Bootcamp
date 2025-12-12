def check_leap_year(year: int) -> bool:
    """Checks whether a year is a leap year or not"""
    if year <= 0:
            raise ValueError("Year cannot be negative.")
    if year % 4 == 0:
        if year % 100 == 0:  #if only divisible by 100 but not 400, its leap year
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False
if __name__ == "__main__":
    try:
        year = int(input("Enter a year: "))
        if year <= 0:
            raise ValueError("Year cannot be negative.")
        if check_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input: Please enter a valid year.")