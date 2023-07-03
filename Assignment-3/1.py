# Output:
# =====================================
# User Name: Bilbo
# Balance: 1.0
# Account Type: Savings
# =====================================
# User Name: Frodo
# Balance: 1.0
# Account Type: Business
# =====================================




class BankAccount:
    
    def __init__(self, user_name, account_type, balance=1.0):
        
        self.user_name = user_name
        self.account_type = account_type    
        self.balance = balance







account1 = BankAccount("Bilbo", "Savings")
print("=====================================")
print(f"User Name: {account1.user_name}")
print(f"Balance: {account1.balance}")
print(f"Account Type:", account1.account_type)
print("=====================================")
account2 = BankAccount("Frodo", "Business")
print(f"User Name: {account2.user_name}")
print(f"Balance: {account2.balance}")
print(f"Account Type: {account2.account_type}")
print("=====================================")

# (ii) Now change the balance of account1 to 15.75 taka and account2 to 700.50 taka. Finally, print the updated details with their respective user names.

# Output:
# New account balance of Bilbo is 15.75
# New account balance of Frodo is 700.5

account1.balance = 15.75
account2.balance = 700.50

print("New account balance of bilbo is", account1.balance, "taka")
print("New account balance of bilbo is", account2.balance, "taka")
