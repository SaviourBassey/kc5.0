# CLASSES IN PYTHON


# an example of that class 


# buit-in classes: str, int, float   (fuunctions) upper,lower


# shield that protect functions for specific types


# Encapsulation, Inheritance, Polymorphism, 


class BankAccount:

    def __init__(self, age, phone, name="hello"):
        self.name = name
        self.age = int(age)
        self.email = name + ".company@gmail.com"
        self.account_bal = 0
        self.account_number = phone

    
    # BankAccount Methods
    def check_balance(self):
        print("You account bal is ------")

    def deposit(self, amount):
        print(self)
        
        self.account_bal = self.account_bal + amount
        print(f"You deposited a sum of  {amount} and you new bal is {self.account_bal}")

    def withdrawal(self, amount):
        print("You withdrew a sum of ------")


class NewClass(BankAccount):
    pass





x = BankAccount(100, 22222222, "person 1")
y = BankAccount(50, 1111111111)
# z = BankAccount("person 3", 20)


z = NewClass()

print(x.name)
print(y.name)
print()
print(x.account_bal)
print(y.account_bal)
print()
print(x.account_number)
print(y.account_number)
print()
y.deposit(1000)
print()
print(y.account_bal)


s = "hello"


