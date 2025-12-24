from account import Account
from account_manager1 import AccountManager1   #program follows SRP (single responsibility principle)
from account_manager2 import AccountManager2


class Program:
    @staticmethod                              #static method: so it is utility/helper method, not related to class much
    def main(args): 
        
        acc = Account()

        print("Performing Account Transactions using Account Manager 1...")
        manager1 = AccountManager1()
        manager1.fill_account_data(acc)   #Managers operate on data #They do not own the data #Loose coupling ✔️
        manager1.display_account_data(acc)
        

        print()

        print("Performing Account Transactions using Account Manager 2...")
        manager2 = AccountManager2()
        manager2.fill_account_data(acc)
        manager2.display_account_data(acc)
        
        input()


if __name__ == "__main__":
    Program.main([])
