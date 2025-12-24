class AccountManager2:
    """
    Method to fill account details into the account object passed
    """
    def fill_account_data(self, acc):
        acc.acc_no = "004701"  #properly uses getters and setter, so no attruibutes are no longer class level, but object level
        acc.name = "Nitesh"            # class level atribute still exist, but are overshdowed
        acc.balance = 45000.0

    """
    Method to display account details from the account object passed
    """
    def display_account_data(self, acc):
        print("AccNo : " + acc.acc_no)
        print("Name : " + acc.name)
        print("Balance : " + str(acc.balance))
