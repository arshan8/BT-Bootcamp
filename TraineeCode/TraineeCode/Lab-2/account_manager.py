class AccountManager:
    """
    Method to store account details into the account object passed
    """
    def fill_account_data(self, acc):  #Bug FIX: Account details are populated through setters, ensuring encapsulation
        acc.acc_no = "004701"            
        acc.name = "Nitesh"          
        acc.balance = 700.0

    """
    Method to display account details from the account object passed
    """
    def display_account_data(self, acc):
        print()
        print("AccNo : " + acc.acc_no)
        print("Name : " + acc.name)
        print("Balance : " + str(acc.balance))
