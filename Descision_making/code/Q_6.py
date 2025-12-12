def check_parity(x : int) -> str:
    """checks whether number is even or odd"""
    if x&1:
        return "odd"
    else:
        return "even"
    

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))  #no need pydantic coercion, number must be integer
        result = check_parity(num)
        print(f"The number {num} is {result}.")
    except ValueError:
        print("Invalid input: Please enter an integer.")

  
