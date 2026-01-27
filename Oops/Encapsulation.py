# Encapsulation in Python

# --------------------------------------------------
# 1. Public Variables Example
# --------------------------------------------------

class Student:
    def __init__(self, name):
        self.name = name   # public variable

student = Student("Jagriti")
print("Public name:", student.name)


# --------------------------------------------------
# 2. Protected Variables Example
# --------------------------------------------------

class Employee:
    def __init__(self, salary):
        self._salary = salary   # protected variable

emp = Employee(50000)
print("Protected salary:", emp._salary)


# --------------------------------------------------
# 3. Private Variables Example
# --------------------------------------------------

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def show_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount


account = BankAccount(1000)

# account.__balance  # ❌ Cannot access private variable directly
account.show_balance()

account.deposit(500)
account.show_balance()


print("\nEncapsulation examples completed.")
