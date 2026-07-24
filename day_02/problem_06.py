class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposite(self,amount):
        self.balance+= amount
        print("amount credited")

    def withdraw(self,amount):
        if amount>self.balance:
            print("insafficient money")
            return
        self.balance-= amount
        print("amount debited")
    def __str__(self):
        return f"owner: {self.owner}, balance: {self.balance}"

account1=BankAccount("debasis_dora",5000)
account1.deposite(5000)
account1.withdraw(2000)
print(account1)

