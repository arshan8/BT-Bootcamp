from pydantic import BaseModel, ValidationError, PositiveFloat

class Number(BaseModel):
    a : PositiveFloat
    b : PositiveFloat
    c : PositiveFloat

def SimpleInterest( p : int, r : int, t : int) -> int:
    return (p*r*t)/100


if __name__ == "__main__":
    try:
        p = input("enter principle amount : ")
        r = input("enter rate of interest ")
        t = input("enter time in years : ")
        inputs = Number(a=p, b=r, c=t)
        interest = SimpleInterest(inputs.a, inputs.b, inputs.c)
        print(f"Simple Interest is : {interest}")
       
    except ValidationError as e:       
        print("invalid input:", e)

