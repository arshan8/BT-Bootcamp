
from Q_25 import Item

class Cart:

   
    promotion_code = "PROMO"  #for Q26


     # item wise discount -> initial grand total -> grand total based discount -> surge amount -> taxe


    def __init__(self, name, membership_type, payment_method):
        self.items = []  #list of items, items = object     
        self.membership_type = membership_type
        self.payment_method = payment_method
        self.customer_name = name
        self.inv = []


    def add_item(self,item):
        self.items.append(item)


    @property
    def grand_total(self):

        total = 0
        for ele in self.items:
            code = ele.code

            #Q_30
            promo_applied_msg = ""

            if len(code) >= len(self.__class__.promotion_code):
                if code[:len(self.__class__.promotion_code)] == self.__class__.promotion_code:
                        item_amt=(ele.total*(1-0.1))  #10%off
                        promo_applied_msg = f"10% off on {ele.total}"
                else:
                    item_amt=(ele.total)

            else:
                item_amt=ele.total
            total+=item_amt

            #Q_32
            self.inv.append(f"item code {ele.code}  Qty: {ele.quantity}  price {ele.price}  {promo_applied_msg}  total = {item_amt}")

        return total
    
    def display_grand_total(self):
        print(f"the total amount before discount is : {self.grand_total}")

    
    #Q_27
    @property   
    def discounted_grand_total(self):
        discounted_total = self.grand_total

        if discounted_total > 10_000:
            discounted_total-=(0.1*discounted_total)

        if sum(item.quantity for item in self.items) > 20:
            discounted_total -= (0.05*discounted_total)

        #Q_28

        if self.membership_type in ["y", "Y"]:
            discounted_total -= (0.02*discounted_total)

        return discounted_total


    def display_discounted_total(self):
        print(f"total amount after discounts: {self.discounted_grand_total}")
        print(f"discounted amount is : {self.grand_total - self.discounted_grand_total}")


    #Q_29

    @property
    def total_after_tax_and_discount(self):
        discounted_total = self.discounted_grand_total


        #Q_31  surcharge amount
        if self.payment_method == "credit card":
            discounted_total+=discounted_total*(0.02)

        if discounted_total < 5_000:
            return discounted_total + discounted_total*0.05
        
        if discounted_total <= 20_000:
            return discounted_total + discounted_total*0.1
        
        if discounted_total > 20_000:
            return discounted_total + discounted_total*0.15
        
        
        return discounted_total
    
        


    def display_after_tax(self):
        print(f"total tax : {self.total_after_tax_and_discount - self.discounted_grand_total}")
        print(f"FInal amount to be payed : {self.total_after_tax_and_discount}")


    #Q_32
    def generate_invoice(self):
        print("-_-_-"*10)
        print(f"Welcome {self.customer_name}")
        if self.total_after_tax_and_discount < 500:
            print("Sorry purchase failed! total bill is too less, mimimum amount is 500")
        else:
            print("\n".join(self.inv))
            self.display_grand_total()
            self.display_discounted_total()
            self.display_after_tax()

            loyal_points = self.total_after_tax_and_discount//100
            print(f"Custome name : {self.customer_name} , loyalty points : {loyal_points}")
        print("-_-_-"*10)


    
if __name__ == "__main__":

    name = input("Enter your name: ")
    membership_type = input("enter membership type (y) :")
    print("select mode of payment")
    while True:
        try:
            payment_method = int(input("enter 1 for cash, 2 for credit card: "))
            payment_methods = ["cash", "credit card"]
            if payment_method <= len(payment_methods):
                payment_method = payment_methods[payment_method-1]
                break
            else:
                print("enter valid payment method")
        except Exception as e:
            print("Error:", e)


    c = Cart(name,membership_type,payment_method)


    for i in range(2):
        item = Item(
                code= input(f"enter code for \" {i+1} \" item: "),
                description=input("enter description : "),
                quantity= input("enter quantity: "),
                price=input("enter price : ")
            )
        c.add_item(item)

    
    c.generate_invoice()


    

    





    