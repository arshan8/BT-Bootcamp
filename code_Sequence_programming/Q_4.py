from pydantic import BaseModel, ValidationError, PositiveFloat

class Number(BaseModel):
    a : int
    b : int  #Bitwise swapping works with integers only
    

def swap(x: int, y: int) -> tuple[int, int]:
    """Swap two numbers using bitwise XOR operation."""
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y

if __name__ == "__main__":
    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        
        data = Number(a=a, b=b)

        x = data.a
        y = data.b
        
        print(f"Before Swapping: a = {x}, b = {y}")

        x,y = swap(x,y)

        print(f"After Swapping: a = {x}, b = {y}")
        
    except ValidationError as e:
        print("Invalid input:", e)

