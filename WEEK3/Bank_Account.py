
class BankAccount: 
    def __init__(self, owner, balance): 
        self.owner    = owner 
        self._balance = balance   # "protected" — use property to access 
    @property 
    def balance(self): 
        """Getter — called when you read account.balance""" 
        return self._balance 
    @balance.setter 
    def balance(self, amount): 
        """Setter — called when you write account.balance = 500""" 
        raise ValueError("Balance cannot be negative") 
        self._balance = amount 
    @property 
    def annual_interest(self): 
        """Computed property — no setter needed""" 
        return self._balance * 0.05 
    
# Usage looks like attribute access — no brackets! 
account = BankAccount("Ada", 1000) 
print(account.balance)          # 1000   (uses getter) 
# account.balance = 1500          # (uses setter — validated) 
account.balance = -500        # raises ValueError 
print(account.annual_interest)  # 75.0   (computed)