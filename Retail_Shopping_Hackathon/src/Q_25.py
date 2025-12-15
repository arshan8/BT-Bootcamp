
from pydantic import BaseModel

class Item(BaseModel):
    code: str
    description: str
    quantity: int
    price: int

    @property
    def total(self):
        return self.price * self.quantity
    
    def display_total_price(self):
        print(self.total)

if __name__ == "__main__":
    try:
        item = Item(
            code= input("enter code : "),
            description=input("enter description : "),
            quantity= input("enter quantity: "),
            price=input("enter price : ")
        )

        print("Item code:", item.code)
        print("Description:", item.description)
        print("Quantity:", item.quantity)
        print("Price:", item.price)

        item.display_total_price()

    except Exception as e:
        print("Error:", e)
    