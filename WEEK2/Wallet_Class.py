# # Class wallet Creation

# class Wallet:
#     def __init__(self, owner):
#         self.owner = owner
#         self.balance = 0

#     def add_money(self, amount):
#         self.balance += amount

#     def __str__(self):
#         return f"{self.owner}'s Wallet: ₦{self.balance}"

#     def __add__(self, other):
#         new_wallet = Wallet("Joint Wallet")
#         new_wallet.balance = self.balance + other.balance
#         return new_wallet

#     def __eq__(self, other):
#         return self.balance == other.balance


# # Testing

# wallet1 = Wallet("Ada")
# wallet1.add_money(500)

# wallet2 = Wallet("John")
# wallet2.add_money(300)

# print(wallet1)
# print(wallet2)

# joint = wallet1 + wallet2
# print(joint)

# print(wallet1 == wallet2)

# # Add Others
# def __add__(self, other):
#     if isinstance(other, Wallet):
#         new_balance = self.balance + other.balance

#         joint_wallet = Wallet("Joint Wallet")
#         joint_wallet.balance = new_balance
#         return joint_wallet

















