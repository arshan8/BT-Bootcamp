
from pydantic import BaseModel, ValidationError, PositiveFloat

class Amount(BaseModel):
    total_amount: PositiveFloat
    discount_percent: PositiveFloat

def calculate_discount(amount: float, discount: float) -> float:
    return (amount * discount) / 100

if __name__ == "__main__":
    try:
        amt = input("Enter total amount: ")
        disc = input("Enter discount percentage: ")
        
        inputs = Amount(total_amount=amt, discount_percent=disc)
        
        discount_value = calculate_discount(inputs.total_amount, inputs.discount_percent)
        final_price = inputs.total_amount - discount_value
        
        print(f"Discount Amount: {discount_value}")
        print(f"Final Price After Discount: {final_price}")

    except ValidationError as e:
        print("Invalid input:", e)
