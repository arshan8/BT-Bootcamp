from pydantic import BaseModel, ValidationError

class Number(BaseModel):
    a : int
    b : int

def add(a : int, b : int) -> int:
    return a + b

def average(a : int, b : int) -> float:
    return (a + b) / 2


if __name__ == "__main__":
    try:
        a = input("enter a: ")
        b = input("enter b: ")
        inputs = Number(a=a, b=b)
        sum = add(inputs.a, inputs.b)
        avg = average(inputs.a, inputs.b)
        print(f"Sum: {sum}, average: {avg}")
    except ValidationError as e:       
        print("invalid input:", e)


print("figured out github project board, issues and how it links")

