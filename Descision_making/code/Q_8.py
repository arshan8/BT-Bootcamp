
def largest_of_three(a: int, b : int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and  b >= c:
        return b
    
    return c

if __name__ == "__main__":
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number: "))
        
        largest = check_largest_of_three(a, b, c)
        print(f"The largest number is {largest}.")
    except ValueError:
        print("Invalid input: Please enter integers only.")


