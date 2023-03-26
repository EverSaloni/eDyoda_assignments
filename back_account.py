class Account:
    def _init_(self, title = None, balance = 0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def _init_(self, title=None, balance=0, interestRate=0):
            super()._init_(title, balance)
            self.interestRate = interestRate

acc = SavingsAccount('Saloni', 2000, 10)
