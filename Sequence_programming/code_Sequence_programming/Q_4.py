from pydantic import BaseModel, ValidationError, PositiveFloat
from Q_1 import Number


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
        
        data = Number(a=a, b=b)  ##Bitwise swapping works with integers only

        x = data.a
        y = data.b
        
        print(f"Before Swapping: a = {x}, b = {y}")

        x,y = swap(x,y)

        print(f"After Swapping: a = {x}, b = {y}")
        
    except ValidationError as e:
        print("Invalid input:", e)

