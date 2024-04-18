# class User:
#     def __init__(self,firstName,lastName,age):
#         self.first = firstName
#         self.last = lastName
#         self.age = age
    
#     def full_name(self):
#         return f'{self.first} {self.last}'
    
#     def initials(self):
#         return f'{self.first[0]}.{self.last[0]}'
    
#     def favorite(self, thing):
#         return f'{self.first} likes {thing}'
    
#     def age_calculate(self):
#         if (self.age >= 50):
#             return f'You are really old {self.first} aging {self.age} what is the secret ?'
#         else:
#             return f'Good {self.first} you have many more years to go'
        
#     def birthday_wishes(self):
#         self.age += 1
#         return f'Happy {self.age}th Birthday {self.first} !!'

# user1 = User('John','Perry',45)
# user2 = User('Johnny','Cena',90)

# print(user1.favorite('Ice cream'))
# print(user2.favorite('Gobi Manchurian'))
# print(user1.initials())
# print(user2.initials())
# print(user2.age_calculate())
# print(user1.age)

# class BankAccount():
#     account_balance = 0
#     def __init__(self,name,balance):
#         self.owner = name
#         BankAccount.account_balance = balance

#     def deposit_amount(self,amount):
#         BankAccount.account_balance += amount
#         return BankAccount.account_balance

#     def withdraw_account(self,withdraw):
#         BankAccount.account_balance -= withdraw
#         return BankAccount.account_balance
    
#     def return_balance(self):
#         return BankAccount.account_balance 
        
# user1 = BankAccount('John',10000)
# user2 = BankAccount('Johnny',20000)

# print(user1.deposit_amount(2000))
# print(user1.withdraw_account(200))

