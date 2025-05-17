class BankAccount:
    
    def __init__(self, initial_balance = 0,interest_rate=0.05):
        self.balance = initial_balance
        self.interest_rate = interest_rate
        self.transactions = []
        self.overdraft_limit = -50

# Depositing money on the account

    def deposit(self,amount):
        """
        adds specified account to the account balance
        """
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited. New balance: ${self.balance}")
            self.transactions.append(f"Deposited ${amount}")
        else:
            print("Deposit amount must be above than zero.")
        
        
        
# Withdrawing money from the account

    def withdraw(self,amount):
        """
        Withdraws specified amount from the account balance.
        """
        if self.balance - amount  >= self.overdraft_limit:

            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")
            self.transactions.append(f"Withdrawn ${amount}")
        else:
            print("Insufficient balance.")
            self.transactions.append(f"Failed withdrawal attempt: ${amount}, Insufficient funds")
            
# Applying interest
    
    def apply_interest(self, ):
        """
        Apply specified interest to the account balance.
        """
        self.balance *= (1 + self.interest_rate)
        new_balance = round(self.balance, 2)
        print(f"Interest Applied! New balance : ${new_balance:.2f}")
        self.transactions.append(f"Applied Interest,New balance:${new_balance:.2f}")

# Adding Transaction feature in the account

    def show_transaction(self):
        """
        Shows the deposit and withdraw history of transaction 
        """
        print("Transaction History")
        for transaction in self.transactions:
            print(transaction)


# They are test cases to identify whether our function works properly or not.

account = BankAccount(100)
account.deposit(0)
account.withdraw(101)
account.apply_interest()
account.show_transaction()
