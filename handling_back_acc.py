class Account:
    def _init_(self, title = None, balance = 0):
        self.title = title
        self.balance = balance

    def getBalance(self):
         return self.balance
    
    def deposit(self, amount):
         self.balance += amount

    def withdrawal(self, amount):
         self.balance -= amount         

class SavingsAccount(Account):
    def _init_(self, title=None, balance=0, interestRate=0):
         super()._init_(title, balance)
    self.interestRate = interestRate

    def interestAmount(self):
         return (self.interestRate * self.balance)/100

demo1 = SavingsAccount("Ashish", 2000, 5)

demo1.deposit(500)
print(demo1.getBalance())

demo1.withdrawal(500)
print(demo1.getBalance())

print(demo1.interestAmount())