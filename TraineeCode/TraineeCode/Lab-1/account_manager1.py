class AccountManager1:
    """
    Method to fill account details into the account object passed
    """
    def fill_account_data(self, acc):
        acc._acc_no = "004701"    #bypass setter, but python wont throw an error, Breaks encapsulation
        acc._name = "Nitesh"        #now it becomes instance level, overshdwoing class level, because acc.__xxx is referring to that instace of the class
        acc._balance = 45000.0

    """
    Method to display account details from the account object passed
    """
    def display_account_data(self, acc):
        print("AccNo : " + acc._acc_no)
        print("Name : " + acc._name)
        print("Balance : " + str(acc._balance))
