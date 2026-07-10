#My class mini project
#BANK ACCOUNT
    
class BankAccount:
    bank_name = "TechRise Bank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"\nDeposited ₦{amount:,.2f}")
        print(f"New balance: ₦{self.balance:,.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError(
                f"Insufficient funds. Current balance: ₦{self.balance:,.2f}"
            )
        self.balance -= amount
        print(f"\nWithdrew ₦{amount:,.2f}")
        print(f"New balance: ₦{self.balance:,.2f}")

    def get_balance(self):
        return self.balance

    def display_info(self):
        print("\n========== ACCOUNT DETAILS ==========")
        print(f"Bank: {self.bank_name}")
        print(f"Owner: {self.owner}")
        print(f"Balance: ₦{self.balance:,.2f}")


class SavingsAccount(BankAccount):
    interest_rate = 0.05

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"\nInterest Added: ₦{interest:,.2f}")
        print(f"New Balance: ₦{self.balance:,.2f}")

    def display_info(self):
        super().display_info()
        print(f"Interest Rate: {self.interest_rate * 100}%")



if __name__ == "__main__":

    print("====== TECHRISE BANK ======\n")

    # User enters details
    owner = input("Enter account owner's name: ")
    balance = float(input("Enter opening balance: ₦"))

    account = SavingsAccount(owner, balance)

    while True:
        print("\n========== MENU ==========")
        print("1. Display Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Add Interest")
        print("5. Check Balance")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        try:
            if choice == "1":
                account.display_info()

            elif choice == "2":
                amount = float(input("Enter deposit amount: ₦"))
                account.deposit(amount)

            elif choice == "3":
                amount = float(input("Enter withdrawal amount: ₦"))
                account.withdraw(amount)

            elif choice == "4":
                account.add_interest()

            elif choice == "5":
                print(f"\nCurrent Balance: ₦{account.get_balance():,.2f}")

            elif choice == "6":
                print("\nThank you for banking with TechRise Bank.")
                break

            else:
                print("Invalid option. Please choose between 1 and 6.")

        except ValueError as e:
            print("Error:", e)