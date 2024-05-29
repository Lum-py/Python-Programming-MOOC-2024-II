# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name: str, account_nr: str, balance: float):
        self.__name = name
        self.__account_nr = account_nr
        self.__balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()
    
    def withdraw(self, amount: float):
        if self.__balance >= amount * 1.01:
            self.__balance -= amount
            self.__service_charge()

    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        self.__balance *= 0.99


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)


