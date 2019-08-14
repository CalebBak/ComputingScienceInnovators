#!/usr/bin/env python3

"""
File:
Name:

Bank account simulation to learn how to use classes in Python
Concepts covered: Classes

Base:       deposit, withdraw, view account
Extension:  (1) chequing/savings (2) savings growth (3) transaction history
"""

__author__      = "Tem Tamre"
__copyright__   = "ttamre@ualberta.ca"


class BankAccount:    
    def __init__(self, name, chq_balance=5000, sav_balance=5000):
        self.name = name
        self.chq_balance = chq_balance
        self.sav_balance = sav_balance
        self.history = ["Created account for %s" % self.name]
    
    def deposit(self, amount, savings=False, _transfer=None):
        if savings:
            self.sav_balance += amount
        else:
            self.chq_balance += amount
        if _transfer != None:
            self.history.append("Recieved $%.2f from %s into %s" % (amount, _transfer, "savings" if savings else "chequing"))
        else:
            self.history.append("Withdrew $%.2f to %s account" % (amount, "savings" if savings else "chequing"))

    def withdraw(self, amount, savings=False, _transfer=None):
        if savings:
            self.sav_balance -= amount
        else:
            self.chq_balance -= amount
        if _transfer != None:
            self.history.append("Transferred $%.2f from %s to %s" % (amount, "savings" if savings else "chequing", _transfer))
        else:
            self.history.append("Withdrew $%.2f to %s account" % (amount, "savings" if savings else "chequing"))
    
    def showAccount(self):
        print("Name:", self.name)
        print("Chequing Balance: $%.2f" % self.chq_balance)
        print("Savings Balance: $%.2f" % self.sav_balance)
        
    def growSavings(self, pct):
        self.sav_balance = round(self.sav_balance * (pct + 1), 2)
        self.history.append("Grew savings by %d%% to $%.2f" % (pct * 100, self.sav_balance))
        
    def transfer(self, account, amount, savings=False):
        self.deposit(amount, savings, account.name)
        account.withdraw(amount, savings, self.name)
        
        
    def printTransactionHistory(self):
        print("\nTransaction history for %s" % self.name)
        print('-'*35)
        for item in self.history:
            print(item)
        print('\n')


def test():
    alex  = BankAccount("Alex")
    bobby = BankAccount("Bobby", 5000, 3250)

    # Testing Alex
    assert alex.name == "Alex"
    assert alex.chq_balance == 5000
    alex.deposit(500)
    alex.deposit(1500)
    alex.withdraw(250.25)
    assert alex.chq_balance == 6749.75
    alex.showAccount()

    # Testing Bobby
    assert bobby.name == "Bobby"
    assert bobby.chq_balance == 5000
    assert bobby.sav_balance == 3250
    bobby.deposit(alex.chq_balance, True)
    bobby.withdraw(500, True)
    bobby.withdraw(1250.50, True)
    assert bobby.sav_balance == 8249.25
    bobby.growSavings(0.05)
    assert bobby.sav_balance == 8661.71
    bobby.showAccount()
    
    bobby.transfer(alex, 2000)
    
    alex.printTransactionHistory()
    bobby.printTransactionHistory()


if __name__ == "__main__":
    test()
    print("Program success!")